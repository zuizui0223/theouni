# Graphify Dissertation Architecture Report

## Purpose

This focused overlay records the novelty-first dissertation traversal. It does not replace the non-linear Worldline Atlas, change the source theorem DAG, or transfer source theorem ownership to `theouni`.

## Thesis

> **When does a scientific representation that is adequate for one ecological task cease to be reusable after capability, future grammar, structural replacement, mechanism responsibility, evidence, target, representation, or domain changes?**

## Summary

- research parts: 4
- source-owned research chapters: 8
- general introduction: 1
- general synthesis: 1
- covered worldlines: 9
- embedded bridge/firewall modules: 4
- hard scientific dependencies: 1
- Graphify-compatible overlay nodes: 71
- Graphify-compatible overlay edges: 80

## Preferred traversal

```text
chapter:introduction
chapter:1
chapter:2
chapter:3
chapter:4
chapter:5
chapter:6
chapter:7
chapter:8
chapter:synthesis
```

## Research parts and chapters

### Part 1 — When Doing More Requires Knowing More

- **Chapter 1 — When Conservation Capacity Outgrows Conservation Knowledge**
  - worldline: worldline:capability
  - source owner: repo:crest
  - embedded module: none
  - forbidden inference: `small intervention or capability gain => small required-state or monitoring burden`
- **Chapter 2 — When Closed Simplicity Fails under Open Futures**
  - worldline: worldline:future
  - source owner: repo:ccoc
  - embedded module: none
  - forbidden inference: `simple exact interfaces under each closed grammar => a simple exact interface under the open grammar`

### Part 2 — When Scientific Laws Fail to Travel

- **Chapter 3 — When Macro-Laws Do Not Survive Ecological Replacement**
  - worldline: worldline:history
  - source owner: repo:mltr
  - embedded module: none
  - forbidden inference: `an exact source macro-law => the same exact macro-law after turnover, recolonization, extinction, or rewiring`
- **Chapter 4 — When Visible Equivalence Fails under Mechanism Uncertainty**
  - worldline: worldline:mechanism
  - source owner: repo:mrm
  - embedded module: none
  - forbidden inference: `same visible state => same deterministic intervention law`

### Part 3 — When More Information Does Not Give the Needed Answer

- **Chapter 5 — When Evidence Does Not License the State We Need**
  - worldline: worldline:evidence
  - source owner: repo:ced
  - embedded module: none
  - forbidden inference: `more, finer, or nominally distinguishing information => a licensed ecological target`
- **Chapter 6 — When Learning the Cause and Licensing the Decision Diverge**
  - worldline: worldline:learning
  - source owner: repo:microdonta
  - embedded module: TU-2
  - forbidden inference: `pattern fit or high causal-learning value => identified cause or licensed decision target`

### Part 4 — When an Early Signal Is Not a Warning

- **Chapter 7 — Which State Actually Generates Functional Loss?**
  - worldline: worldline:loss
  - source owner: repo:eco-genetic-criticality
  - embedded module: TU-3
  - forbidden inference: `raw simulator detail or matching coarse eco-genetic marginals => the correct loss-generating state`
- **Chapter 8 — When an Early Signal Is Not a Warning**
  - worldline: worldline:warning
  - source owner: repo:eco-genetic-warning-extensions
  - embedded module: TU-4
  - forbidden inference: `signal precedes loss => the signal is a valid or portable warning`

## General synthesis

- title: **The Theory Universe: Adequacy Has No Privileged Direction of Travel**
- worldline: worldline:revision
- modules: TU-1, theouni
- forbidden inference: `a representation adequate for the original task => a representation revisable for a later task`

## Embedded module allocation

- `TU-1` -> `chapter:synthesis`
- `TU-2` -> `chapter:6`
- `TU-3` -> `chapter:7`
- `TU-4` -> `chapter:8`

## Hard scientific dependency

- `chapter:7` -> `chapter:8`: `loss_domain_must_be_fixed_warning_blind_before_warning_evaluation`

## Interpretation

```text
Worldline Atlas
    = all scientifically allowed task-indexed traversals

Dissertation architecture
    = the editorial traversal that best exposes non-obvious transport failures
```

The architecture is preferred for novelty, but it is not promoted to a privileged theory order.
