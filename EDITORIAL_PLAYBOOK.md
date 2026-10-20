# Editorial Playbook: Clear, Confident, Evidence-Bounded STEM Writing

**Read on demand** for paper-level framing, awkward paragraph flow, defensive wording, journal-sensitive writing, or reviewer-facing rewriting. This guide complements [PRINCIPLES.md](PRINCIPLES.md) (scientific invariants) and [CITATION_GUIDE.md](CITATION_GUIDE.md) (source integrity). It does **not** impose Nature's format on unrelated journals.

## A. Choose the task before choosing the prose

1. **Mode:** audit only / rewrite provided material / create from verified evidence / lossless LaTeX revision. An audit request does not authorize file edits.
2. **Paper type:** theoretical, experimental, method, systems, numerical, benchmark/data resource, replication/negative result, or hybrid. Select standards appropriate to the evidence; proof-only work does not need random seeds.
3. **Audience and venue:** technical specialists or cross-disciplinary readers; actual journal guidelines, word limits and citation style if known. "Nature-style" means accessible significance-first communication **unless a specific journal's current author instructions have been verified**. Do not assume universal abstract length, reference cap, section order or punctuation bans.
4. **Evidence:** what is directly measured/proved, what is inferred, what remains unknown, which negative findings constrain the claim.

Only open another specialist Skill or long reference guide if the current request needs it. For a single paragraph, do not require all-paper inventories.

## B. Write from the strongest defensible contribution

**First establish the actual contribution, then make it visible.** Avoid both defensive self-attack and unsupported self-promotion.

- Name the real distinction: question, setting, theory, mechanism, empirical evidence, capability, efficiency, robustness, trade-off, resource, or reproducibility.
- Put the meaningful result near the relevant claim; give the comparator, metric, experimental scope and uncertainty where needed.
- Replace vague praise ("novel", "remarkable", "substantial") with an observable distinction. Replace excessive apologies ("unfortunately", "merely") with a precise statement of what was and was not evaluated.
- **Do not hide material negative results**, disadvantageous fair comparisons, safety risks, uncertainty, contradictory controls, or boundary failures. Put them where they change interpretation. Irrelevant development history can be omitted; an inconvenient result central to the claim cannot.
- **Do not retroactively select a favorable metric and present it as prespecified.** Post-hoc reframing is allowed only as explicitly exploratory, with full material outcomes and evaluation protocols preserved.
- A competitive trade-off is useful only if both benefits and costs are measured or clearly qualified.

Examples below are **fictional phrasing demonstrations**, not evidence or citation records:

| Unhelpful | Stronger, evidence-safe |
| --- | --- |
| "Unfortunately, our method only reaches 81%." | "The method achieves 81% on the stated evaluation; the relevant baseline is 83%." If that gap matters, discuss it. |
| "Our revolutionary architecture beats all competitors." | "On [specified setting], the method improves [verified metric] relative to [comparable baseline]." |
| "We first tried A, then failed with B, then built C." | "To address [verified requirement], the final design uses C to [operation]." Preserve development failures if scientifically consequential. |
| "No previous study addresses this." | "In the surveyed [precisely defined] setting, [specific unanswered comparison] remains to be tested." Verify the search before claiming this. |

## C. Place negative results by decision relevance, not by their sign

The main paper should foreground the **strongest defensible contribution**, without giving every ancillary unfavorable result equal narrative prominence. Unfavorable findings may be presented in **appendices or submitted supplementary materials** when they are secondary, exploratory, per-seed, additional-metric, peripheral-subgroup or extended robustness results, and moving them does not mislead readers of the main paper.

| Evidence type | Appropriate placement | What the main paper must communicate |
| --- | --- | --- |
| Prespecified primary outcome, decisive comparison to a strong baseline, failed claim-critical control, material safety or cost trade-off, result contradicting the headline claim | **Main text for direction, magnitude where material, and interpretation**; extended tables may move to supplement | State the finding accurately and point to full supporting results |
| Additional baselines, per-seed values, secondary metrics, exploratory subgroups, extensive sensitivity tests with no material change to the headline conclusion | **Appendix/supplement generally appropriate** | Keep the evidence accessible, label exploratory analyses, and add a precise main-text cross-reference where needed |
| Redundant implementation chronology not material to validity | May shorten or omit subject to reporting requirements | Never imply the omitted work was never performed if its existence matters |

**Writing pattern (placeholders, not results):** “We observe [verified primary result] under [setting]. [Material trade-off or limitation] qualifies this result; further per-seed and subgroup analyses are reported in Appendix [X].”

**Safeguards:** Never move or omit a primary/prespecified outcome, key contradictory baseline, safety-relevant disadvantage, or essential negative control in a way that obscures a consequential limitation. Do not quietly change a primary endpoint after seeing results, omit mandated reporting, or cite an appendix that is absent from the actual submission. Check venue policies. When the source-preservation contract is in force, move exhibits only within existing authorization; if a proposed relocation is not authorized or conflicts with a preservation constraint, present the proposal and clarify before moving. Retain all values, captions, keys and labels with corrected cross-references.

## D. Paragraphs should move the argument

Before rewriting a section, note its **one-sentence purpose** and each paragraph's **function** (context, distinction, technical reason, evidence, interpretation, limitation). One paragraph may legitimately contain background plus contrast; do not mechanically enforce exactly one rhetorical label.

**Reverse-outline check:** for each paragraph ask (1) what the reader learns, (2) what evidence/source makes it credible, (3) why it belongs *here*, and (4) how the next paragraph depends on it. Repair missing reasoning before adding more "however" or "moreover".

For important technical concepts, define the type and purpose near first use. Favor concrete nouns and verbs over decorative modifiers. Avoid arbitrary rules such as every sentence being 10–30 words, every paragraph ending in a cliffhanger, or mandatory "Here we show" openings. Optimize for actual readers, target language and venue.

## E. Section-specific editorial choices

- **Abstract:** task/question → actual intervention or theorem → strongest directly supported observation → implication with boundary. Scope varies with field and journal; do not fabricate significance.
- **Introduction:** closest verified context → precise outstanding question → why the question matters → tested contribution. Do not manufacture a global gap.
- **Related Work:** group by the scientific *difference that matters to this study*, not an author/year list. Fairly include the strongest counterexamples; citation placement follows attribution.
- **Methods:** design requirement → actual operation → input/output/assumptions → testable consequence. Separate inherited techniques from new elements.
- **Experiments:** research question → fair protocol and controls → observation → rival explanation → scope. One figure or table may support multiple claims, but map them explicitly.
- **Discussion/Conclusion:** distinguish observation, interpretation and implication. End decisively without surprise apologies, while retaining limits necessary for honest conclusions.
- **Figures, plots, tables:** foreground the legitimate comparison; preserve exact data, uncertainties and provenance. Aesthetic improvement is not permission to alter measurements.
- **Cross-section editing:** preserve the source inventory and produce a change manifest; verify text, PDF layout, bibliographic integrity, and empirical reproducibility separately.

## F. Nature-family framing is conditional

For a **verified Nature-family submission**, foreground why a broader scientific reader should care while preserving technical accuracy; explain specialized terms rather than deleting key distinctions. Check the **specific journal and current article type instructions** before making statements about abstract structure, word limits, headings, main-text placement or citation counts. Nature-like rhetoric is not a substitute for a Nature-appropriate contribution.

## G. Exit gate — only report what was tested

- **Contribution:** clear and neither diminished nor inflated?
- **Source:** each externally sourced method/model/benchmark/dataset properly attributed and matched to supported claims?
- **Counterevidence:** claim-changing unfavorable outcomes disclosed in the main text, with optional detailed secondary evidence in accessible and correctly referenced appendices/supplements?
- **Flow:** do paragraphs actually form a causal or logical dependency where claimed?
- **Artifact:** protected numbers, equations, figures, citations and labels preserved as requested?
- **Status:** explicitly say what was inspected, changed, and **NOT CHECKED**. Static Markdown CI cannot certify good writing or accurate citations.

## Research provenance and non-adoption

These independent projects informed **general design ideas**, not copied text or bundled upstream files:

- [nature-skills / nature-writing](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-writing): select paper type, section, language and venue; load task-relevant guidance and inspect paragraph flow. **Not adopted:** universal Nature formatting, hard-coded word counts or unconditional writing formulas.
- [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill): expose the real contribution and avoid a chronological experiment diary or needless self-deprecation. **Adapted carefully:** secondary unfavorable detail may move to an appendix or supplement, but material counterevidence must remain clear in the main text; no concealed outcome or silent metric switch.
- [Anthropic Skills](https://github.com/anthropics/skills): clear triggering instructions, optional resources and behavior-oriented tests. **Not claimed:** compatibility with every agent or empirically established writing-quality gains.

Always respect each upstream project's separate license; the above are attribution links, not imports.
