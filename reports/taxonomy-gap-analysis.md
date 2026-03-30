# Taxonomy Gap Analysis: PHIL 4040 Lectures vs. Good-Thinking-Bot Corpus

**Date:** 2026-03-29
**Source:** PHIL 4040 lecture notes W9–W16 (game theory half of Rationality & Strategic Interactions, Spring 2026)
**Method:** Systematic comparison of lecture concepts and problem sets against the 167-code taxonomy

## Summary

The PHIL 4040 game theory lectures cover **40 concepts** not represented in the current
taxonomy, plus **~75–80 problem sets** suitable for adaptation into training records. The
largest gap is social choice theory (entirely absent). Several foundational game-theoretic
concepts (mixed strategies, zero-sum games, signaling, behavioral game theory) are also
missing despite being central to Bert's teaching.

## Pareto Efficiency: A Critical Gap

**Status:** Pareto efficiency appears in 149 corpus records but only as a secondary concept
(mostly in PD and Nash equilibrium records: "the NE is not Pareto optimal"). There is no
dedicated taxonomy code.

**Where it appears in the lectures:**
- **W9:** Formal definition ("no other outcome makes at least one player better off without
  making any player worse off"). Applied to each PD cell. Identified as "the engine of most
  interesting problems in game theory, political philosophy, and institutional design."
- **W10:** Students asked whether each NE is Pareto efficient. Hi-Lo paradox framed as NE
  failing to select Pareto-dominant outcome. QWERTY as equilibrium that is NOT payoff dominant.
- **W12:** Problem 2 asks "Is the SPE Pareto efficient? If not, identify a Pareto improvement."
  Centipede Game: BI predicts (1,0) when (6,5) is available.
- **W14:** Folk Theorem range includes Pareto-efficient mutual cooperation. Evolutionary Stag
  Hunt: Pareto-dominant vs. risk-dominant equilibria.
- **W15:** Arrow's Condition 2 (Weak Pareto) as one of the five conditions. Unanimity respect.

**Recommendation:** Add `C1.3: Pareto efficiency` or `B6.0: Pareto efficiency and social
optimality` as a standalone taxonomy code. Students need to understand Pareto *before* they
can appreciate why the PD NE is troubling, why Arrow needs the Weak Pareto condition, and
why the Folk Theorem range matters. Three sub-concepts:
- Pareto efficiency (no Pareto improvement available)
- Pareto improvement (makes someone better off, no one worse off)
- Pareto dominance (outcome A Pareto-dominates B)

## Full Gap Inventory

### Tier 1: Foundational Concepts (should be in the taxonomy)

These are concepts Bert teaches as core content, with dedicated lecture time and problem sets.

| # | Concept | Lecture | Notes |
|---|---------|---------|-------|
| 1 | **Pareto efficiency / improvement / dominance** | W9, W10, W12, W14, W15 | Foundational; 149 mentions but no code |
| 2 | **Zero-sum games and minimax theorem** | W11 | Vindicates maximin from W2; von Neumann 1928 |
| 3 | **Mixed strategy NE** | W11 | Indifference principle, calculation, behavioral vs. epistemic interpretations |
| 4 | **Signaling games** | W12 | Separating/pooling equilibria, Spence, Zahavi |
| 5 | **Ultimatum Game** | W12, W13 | BI vs. empirical data; cross-cultural variation |
| 6 | **Level-k thinking** | W13 | p-Beauty Contest; bounded strategic reasoning |
| 7 | **Arrow's Impossibility Theorem** | W15 | Five conditions, proof by violation |
| 8 | **Condorcet's Paradox** | W15 | Cyclical preferences as money pump for societies |
| 9 | **Voting systems** | W15 | Plurality, Borda, IRV, approval; characteristic flaws |
| 10 | **Folk Theorem** | W14 | Range of sustainable outcomes; delta threshold |
| 11 | **Commitment devices** | W12 | Physical, contractual, reputational, delegational, moral |
| 12 | **Hawk-Dove game** | W11, W14 | Distinct from PD; mixed ESS |

### Tier 2: Important Supporting Concepts

These appear with significant pedagogical weight but could be folded into existing codes.

| # | Concept | Lecture | Could fold into |
|---|---------|---------|-----------------|
| 13 | Risk dominance vs. payoff dominance | W10 | B7.1 (Stag Hunt) |
| 14 | Best-response method | W10 | B6.2 (Nash equilibrium) |
| 15 | Dominance reasoning in games | W9 | B6.1 or new code |
| 16 | Common knowledge of rationality | W10, W12 | B8.2 (Backward induction) |
| 17 | Trust Game | W13 | New code or B6.1 |
| 18 | Public Goods Game | W13 | C3.1 (Public goods) |
| 19 | Dictator Game | W13 | New code |
| 20 | Grim Trigger strategy | W14 | B10.x (Repeated games) |
| 21 | Discount factor / shadow of the future | W14 | B10.x |
| 22 | Social preference models (Fehr-Schmidt etc.) | W13 | New code |
| 23 | Gibbard-Satterthwaite Theorem | W15 | Fold with Arrow's |
| 24 | Strategic voting | W15 | Fold with voting systems |
| 25 | Cheap talk vs. costly signals | W12 | Fold with signaling |
| 26 | Entry deterrence / incredible threats | W12 | B8.3 (SPE) |

### Tier 3: Specialized / Applied Concepts

These appear in problem sets or as applications but could be lower priority.

| # | Concept | Lecture |
|---|---------|---------|
| 27 | Traveler's Dilemma (Basu 1994) | W9 |
| 28 | Team reasoning (Bacharach, Sugden) | W9, W10 |
| 29 | Hi-Lo Paradox | W10 |
| 30 | Pure coordination games | W10 |
| 31 | Matching Pennies | W10 |
| 32 | Path dependence / QWERTY | W10 |
| 33 | Paradox of Commitment | W12 |
| 34 | Altruistic punishment | W13 |
| 35 | Cross-cultural game theory (Henrich et al.) | W13 |
| 36 | Noisy environments / echo effects | W14 |
| 37 | Generous TFT / Win-Stay-Lose-Shift | W14 |
| 38 | Replicator dynamics / basins of attraction | W14 |
| 39 | Wolf's Dilemma (N-player cooperation) | W14 |
| 40 | PT applied to games (reference-dependent strategic payoffs) | W9, W10, W11, W14 |

## Problem Sets Available for Adaptation

Each lecture (W9–W16) contains 7–12 multi-part problems spanning three difficulty levels:

| Lecture | Problems | Best for drill | Best for what-if | Best for puzzle |
|---------|----------|----------------|------------------|-----------------|
| W9 | 11 | PD identification from matrices | Payoff modification effects | AI alignment as PD |
| W10 | 12 | NE finding (best-response) | PT in Stag Hunt | Hi-Lo paradox |
| W11 | 11 | Mixed NE calculation | PT probability weighting | Paradox of mixed strategy rationality |
| W12 | 12 | BI on game trees | Commitment devices | Paradox of perfect rationality |
| W13 | 10 | Level-k computation | Loss aversion in Ultimatum | Engineering vs. Application Failure |
| W14 | 10 | Grim Trigger delta calc | Noise and echo effects | Why does cooperation exist? |
| W15 | 10 | Voting system comparison | IIA violation in practice | Arrow's limits of collective rationality |
| W16 | 5 | -- | -- | Grand synthesis problems |

**Total:** ~81 problems, many multi-part. These are Bert's own problems with his pedagogical
style already embedded (ideal-to-real arc, experience before description, three-tier
difficulty). They are the highest-quality source available for expanding the corpus.

## Recommended Next Steps

1. **Add Pareto efficiency** as a standalone taxonomy code (C1.3 or B6.0)
2. **Add Tier 1 concepts** as new taxonomy codes (~12 codes, bringing total to ~179)
3. **Adapt W9–W15 problem sets** into training records — these are Bert's own problems with
   his pedagogical voice, making them higher quality than synthetic generation
4. **Social choice theory** (Arrow's, Condorcet, voting systems) is an entirely missing track
   that could become a 6th content track alongside logic, DT, GT, microecon, and biases
