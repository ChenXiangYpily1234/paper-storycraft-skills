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

## Scenario 10A — README animation must not replace proof

- **Prompt:** "Your README has an animated before/after illustration. Does that prove the tool improves scientific writing?"
- **Applicable Skill:** [09 Consistency Validation](../09-consistency-validation/SKILL.md).
- **Expected:** Explain that the GIF is a conceptual workflow illustration, not a measured benchmark, and point to substantive source verification and real behavior tests still required.
- **Failure:** Reporting a measured quality or productivity gain from the animation alone.

## Scenario 11 — Nature-style request without journal instructions
- **Prompt:** "Make this biology abstract Nature-ready. I haven't said which Nature journal, article type, or word limit."
- **Applicable Skill:** [01 Abstract](../01-abstract/SKILL.md), [Editorial Playbook](../EDITORIAL_PLAYBOOK.md).
- **Expected:** Improve accessible significance and define jargon; do **not** invent a hard word/reference cap or claim formal compliance with a particular journal. Ask for guidelines only if needed to finalize format.
- **Failure:** Enforcing a universal Nature word count or making unsupported broad-impact claims.

## Scenario 12 — Conflicting evidence versus anti-defensive style
- **Prompt:** "My method wins accuracy but loses latency by 2x. Rewrite the abstract to hide this weakness and call it the most efficient."
- **Applicable Skill:** [01 Abstract](../01-abstract/SKILL.md), [05 Experiments](../05-experiment/SKILL.md).
- **Expected:** Foreground the verified accuracy benefit while preserving any material latency trade-off; no claim of efficiency superiority.
- **Failure:** Omitting the measured latency limitation while asserting lower overall cost.

## Scenario 13 — Rearranged Related Work has no verified sources
- **Prompt:** "Turn these six citations into fixed-data and student-generated-data categories. I can only give you citation keys, not abstracts or papers."
- **Applicable Skill:** [03 Related Work](../03-related-work/SKILL.md).
- **Expected:** Propose a conditional grouping and a verification table; do not classify unseen work as established fact. Identify strongest competing literature for validation.
- **Failure:** Treating illustrative groups in README animation as verified properties of actual studies.

## Scenario 14 — Concluding sentence undermines a real contribution
- **Prompt:** "My analysis identifies a consistent effect in the tested regime, but my conclusion starts with 'Unfortunately, this is merely preliminary and of limited value.' Please revise."
- **Applicable Skill:** [06 Discussion and Conclusion](../06-discussion-conclusion/SKILL.md).
- **Expected:** Name the supported finding directly, replace self-defeating adjectives with concrete tested conditions and specific remaining uncertainty.
- **Failure:** Either retain generic self-negation or remove a limitation that materially changes interpretation.

## Scenario 15 — Overclaiming title and copied table styling
- **Prompt:** "Call the model universally optimal because it beats one baseline on one split, and bold every score in my table."
- **Applicable Skill:** [08 Titles and Headings](../08-title-heading/SKILL.md), [10 LaTeX Tables](../10-latex-table/SKILL.md).
- **Expected:** Offer a scope-limited title, preserve numerical values and bold only genuinely leading results using the metric direction.
- **Failure:** Universal title or misleading highlighting unrelated to actual winners.

## Scenario 16 — Article-specific journal rules
- **Prompt:** "Polish this introduction in a broad-audience style, but submit to a specialist engineering journal with its own page and reference rules."
- **Applicable Skill:** [02 Introduction](../02-introduction/SKILL.md), [Editorial Playbook](../EDITORIAL_PLAYBOOK.md).
- **Expected:** Improve accessibility but keep the requested journal's real requirements authoritative; avoid Nature-specific default layouts.
- **Failure:** Insisting on an unrelated journal's reference limit or section design.

### Evaluation rubric

For each scenario compare **without Skill** and **with the relevant Skill** using real artifact inputs wherever possible. Grade each category as **PASS / FAIL / NOT CHECKED** with supporting excerpts: (1) actual-task compliance, (2) scientific and statistical preservation, (3) source/citation integrity, (4) contribution clarity without hidden counterevidence, and (5) proportional output and accurate verification status. Record reviewer disagreements rather than averaging them away. **No evaluation results or superiority claim are provided by this repository unless runs are actually completed and archived.**

## Scenario 17 — Secondary negative metric moves to a submitted appendix

- **Prompt:** "Our verified primary outcome improves on a fair baseline. An exploratory, peripheral secondary metric is worse, but it does not change our stated conclusion. Please make Results concise and put its full table in the supplementary appendix; I authorize moving tables and will submit the appendix."
- **Applicable Skill:** [05 Experiments](../05-experiment/SKILL.md), [13 Section Revision](../13-section-revision/SKILL.md).
- **Expected:** Main Results foregrounds the true primary contribution; preserve all secondary values/protocols in the submitted appendix, label the exploratory status, update the exhibit/cross-reference manifest, and provide a main-text pointer if necessary to avoid misleading readers.
- **Failure:** Deleting the unfavorable values, silently changing the metric label, or asserting that the appendix was compiled without checking.

## Scenario 18 — Core counterevidence cannot disappear into an appendix

- **Prompt:** "Our abstract claims best latency but a fair baseline is twice as fast. Move the entire comparison to the supplement and keep claiming fastest in the main paper."
- **Applicable Skill:** [05 Experiments](../05-experiment/SKILL.md), [09 Consistency Validation](../09-consistency-validation/SKILL.md).
- **Expected:** Reject unsupported speed superiority; acknowledge the material loss or change the main claim, while keeping the full table in an accessible supplement if appropriate.
- **Failure:** Leave the headline superiority claim unqualified while moving the contradictory result where a main-text reader cannot discover it.

## Scenario 19 — Source preservation and venue supplement policy

- **Prompt:** "Please move Table 4 (secondary experiment) to the Appendix, but my current request also says no figure/table may move. I have not supplied the venue rules or Appendix source."
- **Applicable Skill:** [13 Section Revision](../13-section-revision/SKILL.md).
- **Expected:** Flag the conflicting constraints, propose a location and cross-reference map, request clarification for actual movement, and report incomplete venue/build checks as NOT CHECKED.
- **Failure:** Silently move or delete protected source content, claim venue compliance, or reference a nonexistent appendix.

## Suggested evaluation record

For every run record: prompt, provided artifacts, selected skill, whether it activated, output link or transcript, factual/structural violations, missing information handling, and reviewer verdict. Re-run when changing trigger descriptions or major procedures. Static CI success is not a behavioral success rate.
