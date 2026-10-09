---
name: discussion-conclusion-story
description: Interpret evidence, articulate scientific and practical implications, report limitations, and close the paper without overstating what was demonstrated.
---

# Discussion, Limitations, and Conclusion

Read [PRINCIPLES.md](../PRINCIPLES.md). This Skill produces an evidence-aligned narrative ending, not a second abstract or a place to quietly introduce unsupported contributions.

## 1. Derive the ending from the opening question

List the question and contributions promised in the Introduction. For each one, find its direct proof, analysis, or experimental evidence, plus material counterexamples. If there is a mismatch, revise either the promise or conclusion; do not paper over it with confident wording.

Build an ending map: **question → key observed result → warranted interpretation → scientific/practical implication → boundary → next research question**.

## 2. Distinguish functions

**Discussion** interprets why observations may matter, compares alternative explanations, separates what was established from what is plausible, discusses methodological trade-offs, and explores transfer conditions.

**Limitations/Threats to validity** state conditions under which results may differ, assumptions that matter, missing controls, external validity, and the scientific effect of those uncertainties. Do not bury a central threat in a generic list.

**Conclusion** closes the original question with a short, accurately scoped takeaway. It should not introduce a new theorem, new metric, new mechanism, or previously unseen headline result.

The paper may combine or separate these sections depending on content and requirements.

## 3. Make claims proportional to evidence

Differentiate:
- a reported observation from an explanation of its cause;
- a component's measured contribution from universal necessity;
- association from causal identification;
- success under specified information access from unrestricted performance;
- no detected difference from equivalence;
- a valid theorem under assumptions from an unconstrained guarantee;
- a result on tested data from out-of-distribution or deployment generalization.

When an independent alternative works, its success does not imply that an original model component was internally replaced. If a recovery attempt fails, necessity remains unresolved unless a stronger identification argument exists.

## 4. State useful scope along multiple dimensions

Relevant boundaries may include population and sampling, task and output space, dataset version, train–test split, hardware and runtime environment, model capacity, pretrained information, resource budget, statistical power, failure handling, adversarial inputs, and proof assumptions.

Only mention dimensions actually relevant to the central claim. Explain *how* a limitation affects interpretation, not just that it exists.

## 5. Treat negative evidence explicitly

Acknowledge important counterexamples and heterogeneous groups. Avoid replacing "one material failure occurred" with a misleading "almost always succeeds." Distinguish inconclusive, underpowered, mixed, and directly contrary results.

A failure can motivate a new experiment; it cannot automatically establish its preferred causal explanation. Proposed future experiments must be presented as future work, not as already completed evidence.

## 6. Derive future work from the identified boundary

A good next step tests a specific unresolved explanation, new condition, stronger baseline, or deployment constraint. Avoid interchangeable closing lines such as "we will explore more domains" unless the reason and intended test are concrete.

## 7. Cross-document closure checks

Verify that the conclusion's subject, comparison target, primary metric, strongest number, and conditions match title, abstract, Introduction, Results, main figure, and terminology ledger. Conclusions should emphasize scientific meaning, not restate every row of results.

## Make the last three steps distinct

**Results:** report the supported observation and its boundaries. **Discussion:** interpret the evidence, rival explanations and scope (including proof assumptions or physical-validation limits). **Conclusion:** directly answer the opening question in concise scientific language. Do not repeat every figure result or describe weaker subgroup performance as inability to operate. A negative result marks the limits of the tested approach; it is not automatic proof that a particular mechanism is necessary.

## Required outputs

Provide an opening-to-ending claim mapping, Discussion and Conclusion revision plan, full revised text when requested, an evidence-strength audit, important limitations and alternative explanations, and unresolved verification items.

**Acceptance:** The conclusion answers the opening question in language a reviewer can defend using only the paper's actual evidence and declared assumptions.
