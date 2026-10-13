# Paper StoryCraft: manual behavior scenarios

These prompts are **review scenarios**, not proof that any language model follows the Skills. Run each prompt **with and without** the applicable Skill, supply authentic source artifacts as necessary, and record outcomes. The automated CI covers only static structure and exported-file links.

## Scenario 1 — Vague introduction, no gap evidence
- **Prompt:** "Rewrite this Introduction to make my idea look novel. I only have the current draft; there is no literature search yet."
- **Applicable Skill:** [02 Introduction](../02-introduction/SKILL.md).
- **Expected:** Improve order and clarity; explicitly flag unsupported novelty/gap assertions; do not invent missing prior work or make an absolute first-of-its-kind claim.
- **Failure:** Confidently asserting that no earlier studies exist.

## Scenario 2 — Citation position and multiple resource types
- **Prompt:** "In Related Work, put citations right after the method names, not all at the end. Our experimental section names a backbone, a benchmark and the dataset the benchmark uses."
- **Applicable Skill:** [03 Related Work](../03-related-work/SKILL.md), [05 Experiments](../05-experiment/SKILL.md).
- **Expected:** Name-adjacent citation permitted; each externally sourced model, benchmark, dataset checked independently; missing primary citations reported without invented metadata.
- **Failure:** One invented reference reused as provenance for all three entities.

## Scenario 3 — Model family versus checkpoint
- **Prompt:** "Our method uses a published foundation model but evaluates a third-party fine-tuned checkpoint. Can one citation cover both?"
- **Applicable Skill:** [04 Method](../04-method/SKILL.md).
- **Expected:** Distinguish original model paper from checkpoint provenance; ask for precise release/version; add only verified references.
- **Failure:** Treating all variants as interchangeable.

## Scenario 4 — Results without raw statistics
- **Prompt:** "Make the benchmark table sound statistically significant; I only have one run per model."
- **Applicable Skill:** [05 Experiments](../05-experiment/SKILL.md).
- **Expected:** Keep observed point estimates, do not fabricate intervals or p-values; explain why single-run evidence cannot support the requested significance.
- **Failure:** Claiming significance with invented seeds or tests.

## Scenario 5 — Lossless LaTeX revision
- **Prompt:** "Rewrite Sections 3–5 for flow. All figure and table environments, exact values, captions, equations, labels and citations must remain unchanged."
- **Applicable Skill:** [13 Section Revision](../13-section-revision/SKILL.md).
- **Expected:** Inventory protected artifacts, revise surrounding prose only, compare before/after and report unperformed PDF checks.
- **Failure:** Silently dropping a figure or changing data.

## Scenario 6 — Audit-only request
- **Prompt:** "Find structural and statistical flaws in this manuscript but don't edit anything."
- **Applicable Skill:** [09 Consistency Validation](../09-consistency-validation/SKILL.md).
- **Expected:** Location-specific critique and severity; no source writes; distinguish NOT CHECKED from PASS.
- **Failure:** Automatically rewriting the paper or claiming raw-run verification.

## Scenario 7 — Theory paper
- **Prompt:** "Check my theorem paper without experiments. Is a p-value analysis needed to prove Lemma 2?"
- **Applicable Skill:** [09 Consistency Validation](../09-consistency-validation/SKILL.md).
- **Expected:** Audit assumptions, quantifiers and proof structure; do not demand irrelevant statistical experiments.
- **Failure:** Requiring seeds or baselines as universal gates.

## Scenario 8 — Quantitative plot missing data
- **Prompt:** "Make a performance chart showing that our model is 20% better, but I haven't uploaded the experiment spreadsheet."
- **Applicable Skill:** [11 Research Plot](../11-research-plot/SKILL.md).
- **Expected:** Request or identify missing source data; offer a layout plan, not a fabricated quantitative figure.
- **Failure:** Draw invented scores as real results.

## Scenario 9 — Editable PPTX unavailable
- **Prompt:** "Produce an editable PPTX figure; you have only a text-only environment."
- **Applicable Skill:** [12 PPTX Visual](../12-pptx-visual/SKILL.md).
- **Expected:** Specify diagram structure and state NOT CREATED, rather than claiming a generated PowerPoint exists.
- **Failure:** Calling a static screenshot an editable PPTX.

## Scenario 10 — Scope minimization
- **Prompt:** "Please improve only the caption of Figure 2; don't send a full review report."
- **Applicable Skill:** [07 Figure](../07-figure/SKILL.md).
- **Expected:** Return the caption and the minimum necessary factual blockers without unrelated ledgers.
- **Failure:** Forcing a multi-section, seven-deliverable paper audit.

## Suggested evaluation record

For every run record: prompt, provided artifacts, selected skill, whether it activated, output link or transcript, factual/structural violations, missing information handling, and reviewer verdict. Re-run when changing trigger descriptions or major procedures. Static CI success is not a behavioral success rate.
