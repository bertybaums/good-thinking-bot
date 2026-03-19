"""
Unified LLM client that routes requests to Anthropic or MindRouter.

Design principle: Anthropic for quality, MindRouter for volume.

Both backends expose an OpenAI-compatible chat completions interface.
Anthropic is accessed via the anthropic SDK; MindRouter via openai SDK
pointed at the campus HPC endpoint.
"""

from __future__ import annotations

import asyncio
import json
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import anthropic
import openai

from config import (
    ANTHROPIC_API_KEY,
    ANTHROPIC_MAX_CONCURRENT,
    ANTHROPIC_MODELS,
    MAX_RETRIES,
    MINDROUTER_API_KEY,
    MINDROUTER_BASE_URL,
    MINDROUTER_MAX_CONCURRENT,
    MINDROUTER_MODELS,
    RETRY_BACKOFF_BASE,
)

logger = logging.getLogger(__name__)


class Provider(str, Enum):
    ANTHROPIC = "anthropic"
    MINDROUTER = "mindrouter"


@dataclass
class LLMResponse:
    """Standardized response from either provider."""

    content: str
    model: str
    provider: Provider
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: float = 0.0
    raw: Any = field(default=None, repr=False)


class LLMClient:
    """
    Unified sync client for Anthropic and MindRouter.

    Usage:
        client = LLMClient()

        # Quality-sensitive work (anchors, verification)
        response = client.complete(
            messages=[{"role": "user", "content": "..."}],
            task="anchor",  # maps to claude-opus-4-6
        )

        # Bulk work (generation, cross-validation)
        response = client.complete(
            messages=[{"role": "user", "content": "..."}],
            task="bulk_gen",  # maps to gpt-oss-120b on MindRouter
        )
    """

    # Map task names to (provider, model)
    TASK_ROUTING: dict[str, tuple[Provider, str]] = {
        # Anthropic tasks
        "anchor": (Provider.ANTHROPIC, ANTHROPIC_MODELS["anchor"]),
        "verify": (Provider.ANTHROPIC, ANTHROPIC_MODELS["verify"]),
        # MindRouter tasks
        "bulk_gen": (Provider.MINDROUTER, MINDROUTER_MODELS["bulk_gen"]),
        "cross_val": (Provider.MINDROUTER, MINDROUTER_MODELS["cross_val"]),
        "adapt": (Provider.MINDROUTER, MINDROUTER_MODELS["adapt"]),
    }

    def __init__(self) -> None:
        # Anthropic client
        self._anthropic = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        # MindRouter client (OpenAI-compatible)
        self._mindrouter = openai.OpenAI(
            api_key=MINDROUTER_API_KEY,
            base_url=MINDROUTER_BASE_URL,
        )

    def complete(
        self,
        messages: list[dict[str, str]],
        task: str,
        *,
        system: str | None = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        json_mode: bool = False,
    ) -> LLMResponse:
        """
        Send a chat completion request, routed by task name.

        Args:
            messages: Chat messages [{"role": "user", "content": "..."}]
            task: Task name from TASK_ROUTING (e.g. "anchor", "bulk_gen")
            system: Optional system prompt
            temperature: Sampling temperature
            max_tokens: Maximum output tokens
            json_mode: Request JSON output (provider-dependent)

        Returns:
            LLMResponse with content and metadata
        """
        if task not in self.TASK_ROUTING:
            raise ValueError(
                f"Unknown task '{task}'. Valid tasks: {list(self.TASK_ROUTING.keys())}"
            )

        provider, model = self.TASK_ROUTING[task]

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                start = time.monotonic()
                if provider == Provider.ANTHROPIC:
                    response = self._call_anthropic(
                        messages, model, system, temperature, max_tokens, json_mode
                    )
                else:
                    response = self._call_mindrouter(
                        messages, model, system, temperature, max_tokens, json_mode
                    )
                response.latency_ms = (time.monotonic() - start) * 1000
                return response

            except (
                anthropic.RateLimitError,
                anthropic.APITimeoutError,
                openai.RateLimitError,
                openai.APITimeoutError,
            ) as e:
                wait = RETRY_BACKOFF_BASE**attempt
                logger.warning(
                    f"[{provider.value}] Attempt {attempt}/{MAX_RETRIES} failed: {e}. "
                    f"Retrying in {wait:.1f}s..."
                )
                time.sleep(wait)

            except (anthropic.APIError, openai.APIError) as e:
                logger.error(f"[{provider.value}] API error: {e}")
                raise

        raise RuntimeError(
            f"All {MAX_RETRIES} attempts failed for task '{task}' on {provider.value}"
        )

    def _call_anthropic(
        self,
        messages: list[dict[str, str]],
        model: str,
        system: str | None,
        temperature: float,
        max_tokens: int,
        json_mode: bool,
    ) -> LLMResponse:
        """Call Anthropic Messages API."""
        kwargs: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        if system:
            kwargs["system"] = system

        response = self._anthropic.messages.create(**kwargs)

        content = response.content[0].text
        return LLMResponse(
            content=content,
            model=model,
            provider=Provider.ANTHROPIC,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            raw=response,
        )

    def _call_mindrouter(
        self,
        messages: list[dict[str, str]],
        model: str,
        system: str | None,
        temperature: float,
        max_tokens: int,
        json_mode: bool,
    ) -> LLMResponse:
        """Call MindRouter via OpenAI-compatible API."""
        full_messages = []
        if system:
            full_messages.append({"role": "system", "content": system})
        full_messages.extend(messages)

        kwargs: dict[str, Any] = {
            "model": model,
            "messages": full_messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}

        response = self._mindrouter.chat.completions.create(**kwargs)

        choice = response.choices[0]
        usage = response.usage
        return LLMResponse(
            content=choice.message.content or "",
            model=model,
            provider=Provider.MINDROUTER,
            input_tokens=usage.prompt_tokens if usage else 0,
            output_tokens=usage.completion_tokens if usage else 0,
            raw=response,
        )


class AsyncLLMClient:
    """
    Async version for batch processing with concurrency control.

    Usage:
        async with AsyncLLMClient() as client:
            results = await client.batch_complete(
                requests=[
                    {"messages": [...], "task": "bulk_gen"},
                    {"messages": [...], "task": "bulk_gen"},
                ],
            )
    """

    def __init__(self) -> None:
        self._anthropic = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)
        self._mindrouter = openai.AsyncOpenAI(
            api_key=MINDROUTER_API_KEY,
            base_url=MINDROUTER_BASE_URL,
        )
        self._semaphores = {
            Provider.ANTHROPIC: asyncio.Semaphore(ANTHROPIC_MAX_CONCURRENT),
            Provider.MINDROUTER: asyncio.Semaphore(MINDROUTER_MAX_CONCURRENT),
        }

    async def __aenter__(self) -> AsyncLLMClient:
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self._anthropic.close()
        await self._mindrouter.close()

    async def complete(
        self,
        messages: list[dict[str, str]],
        task: str,
        *,
        system: str | None = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        json_mode: bool = False,
    ) -> LLMResponse:
        """Async version of LLMClient.complete with semaphore-based concurrency."""
        if task not in LLMClient.TASK_ROUTING:
            raise ValueError(f"Unknown task '{task}'")

        provider, model = LLMClient.TASK_ROUTING[task]
        semaphore = self._semaphores[provider]

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                async with semaphore:
                    start = time.monotonic()
                    if provider == Provider.ANTHROPIC:
                        response = await self._call_anthropic(
                            messages, model, system, temperature, max_tokens
                        )
                    else:
                        response = await self._call_mindrouter(
                            messages, model, system, temperature, max_tokens, json_mode
                        )
                    response.latency_ms = (time.monotonic() - start) * 1000
                    return response

            except (
                anthropic.RateLimitError,
                anthropic.APITimeoutError,
                openai.RateLimitError,
                openai.APITimeoutError,
            ) as e:
                wait = RETRY_BACKOFF_BASE**attempt
                logger.warning(
                    f"[{provider.value}] Attempt {attempt}/{MAX_RETRIES}: {e}. "
                    f"Retrying in {wait:.1f}s..."
                )
                await asyncio.sleep(wait)

        raise RuntimeError(f"All {MAX_RETRIES} attempts failed for task '{task}'")

    async def _call_anthropic(
        self,
        messages: list[dict[str, str]],
        model: str,
        system: str | None,
        temperature: float,
        max_tokens: int,
    ) -> LLMResponse:
        kwargs: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        if system:
            kwargs["system"] = system

        response = await self._anthropic.messages.create(**kwargs)
        content = response.content[0].text
        return LLMResponse(
            content=content,
            model=model,
            provider=Provider.ANTHROPIC,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            raw=response,
        )

    async def _call_mindrouter(
        self,
        messages: list[dict[str, str]],
        model: str,
        system: str | None,
        temperature: float,
        max_tokens: int,
        json_mode: bool,
    ) -> LLMResponse:
        full_messages = []
        if system:
            full_messages.append({"role": "system", "content": system})
        full_messages.extend(messages)

        kwargs: dict[str, Any] = {
            "model": model,
            "messages": full_messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}

        response = await self._mindrouter.chat.completions.create(**kwargs)
        choice = response.choices[0]
        usage = response.usage
        return LLMResponse(
            content=choice.message.content or "",
            model=model,
            provider=Provider.MINDROUTER,
            input_tokens=usage.prompt_tokens if usage else 0,
            output_tokens=usage.completion_tokens if usage else 0,
            raw=response,
        )

    async def batch_complete(
        self,
        requests: list[dict[str, Any]],
        *,
        on_progress: Any | None = None,
    ) -> list[LLMResponse | Exception]:
        """
        Process multiple requests concurrently with semaphore-based rate limiting.

        Args:
            requests: List of dicts with keys matching complete() parameters
            on_progress: Optional callback(completed_count, total_count)

        Returns:
            List of LLMResponse or Exception for each request
        """
        total = len(requests)
        completed = 0
        results: list[LLMResponse | Exception] = [None] * total  # type: ignore

        async def _process(idx: int, req: dict) -> None:
            nonlocal completed
            try:
                result = await self.complete(**req)
                results[idx] = result
            except Exception as e:
                logger.error(f"Request {idx} failed: {e}")
                results[idx] = e
            finally:
                completed += 1
                if on_progress:
                    on_progress(completed, total)

        await asyncio.gather(*[_process(i, req) for i, req in enumerate(requests)])
        return results
