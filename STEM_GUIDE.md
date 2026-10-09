# STEM Research Writing Guide

**Scope:** Mathematics, theoretical sciences, physics, chemistry, biology, earth and environmental science, materials, engineering, computer science, numerical simulation, and related *technical* interdisciplinary research. This guide does **not** attempt to cover humanities, law, or non-technical social-science scholarship.

Read alongside [PRINCIPLES.md](PRINCIPLES.md) and [WORKFLOW.md](WORKFLOW.md). The goal is a sound argument that a competent reader can follow, **not** a universal chapter layout or a mandatory experiment count.

## 1. Choose the evidence route before drafting

| STEM research type | Warrant for the main claim | Story sequence | Common error |
| --- | --- | --- | --- |
| Mathematics / theoretical computing | Assumptions, definitions, theorem, proof, counterexample | question → assumptions → claim → proof idea → proof → scope | Changing quantifiers or mistaking simulations for proofs |
| Laboratory and field science | Observations, controlled studies, calibrated measurements | phenomenon → uncertainty → question → design → findings → rival explanations | Claiming a mechanism from association |
| Engineering and systems | Actual constraints, system design, reliability and tests | requirement → design choice → operation → evaluation → failure regimes | Listing components without why they are needed |
| Numerical simulation | Model equations, solver, convergence, verification, validation | model → approximation → solver → verification → external checks → uncertainty | Confusing numerical convergence with physical accuracy |
| ML / data-driven methods | Appropriate baselines, tasks, metrics, sampling and uncertainty | gap → method → strong comparison → mechanism/sensitivity → boundaries | Equating best mean score with formal superiority |
| Benchmark, dataset or instrument | Construction, calibration, representativeness, documented use | measurement gap → protocol → validation → applications → limitations | Equating size with validity |
| Replication / negative results / auditing | Fidelity to the target, discriminating test, uncertainty | original claim → protocol → outcome → interpretation → boundary | Equating failed recovery with proof of necessity |
| STEM interdisciplinary work | Explicit integration of multiple valid evidence routes | joint question → distinct methods → integration → limits | Combining incompatible units and inferential standards |

Pick the applicable route; combinations are allowed. No chapter name, number of experiments, or page limit is imposed by this repository.

## 2. First-reader argument spine

1. **Opening tension:** a physical phenomenon, engineering problem, theoretical question, or apparently persuasive inference. State what strong existing results do **not** yet establish.
2. **Research gap:** distinguish a missing comparison, unknown mechanism, unproved theorem, unresolved measurement, or a concrete constraint. Do not manufacture consensus.
3. **Method or proof:** explain the needed design property before naming a module; explain the question each equation, assumption, instrument, solver or operation answers.
4. **Evidence:** present decisive comparisons, proof dependencies, measurements or numerical checks. Organize empirical studies as **capability → controlled test → explanation/robustness → boundary** when suitable.
5. **Interpretation:** distinguish observed result from causal mechanism, simulation from physical validation, approximate match from statistical equivalence, and descriptive subgroup behavior from a proven failure.
6. **Conclusion:** answer the question directly. Do not relist all results or repeat the Discussion's entire list of limitations.

**Read paragraphs in order.** The next paragraph must advance the question raised by the previous one, not simply add another disconnected citation, component or experiment. Define unfamiliar terms and symbols in their first sentence or an immediately adjacent one.

## 3. Claim–evidence–scope ledger

| Claim | Support | Necessary limitation |
| --- | --- | --- |
| Mathematical result | Verified proof under explicit assumptions | Domain, edge cases, quantifiers |
| Experimental observation | Calibrated measurement, sampling and uncertainty | Conditions, controls, validity of instrument |
| Engineering performance | Representative workloads and resource/cost measurements | Hardware, settings, load and failure regime |
| Numerical result | Solver verification, convergence and where possible validation | Discretization and modeling assumptions |
| Benchmark superiority | Fair protocol, paired tests when claimed, proper statistical unit | Datasets, budgets, multiplicity and generalization |
| Recovery without a mechanism | Independent alternative and declared information protocol | Not a causal intervention on the original model |

Never invent data, citations, controls, numerical results, theorems or proofs. If underlying results or rendered diagrams are unavailable, record the review as **not performed**, not PASS.

## 4. Visual and format decision

Use [07-figure](07-figure/SKILL.md) only if a schematic, apparatus plan, pipeline or proof-dependency figure answers a real question. Prefer improving a useful existing overview rather than adding a redundant framework graphic. Use [10-latex-table](10-latex-table/SKILL.md), [11-research-plot](11-research-plot/SKILL.md) and [12-pptx-visual](12-pptx-visual/SKILL.md) when their formats add meaning. The editable **Skills flowchart** is rendered by GitHub from Mermaid in [WORKFLOW.md](WORKFLOW.md).

## 5. STEM-specific final validation

- **Theory:** proof completeness, theorem assumptions, logical dependencies, counterexamples.
- **Measurement:** units, instrument calibration, experimental unit, replicate definition and uncertainty.
- **Simulation:** equations, parameter ranges, convergence and verification versus external validation.
- **Engineering:** workloads, cost, interfaces, failure handling and operational boundary.
- **Statistical evaluation:** population, denominators, paired/unpaired design, uncertainty, selection and multiplicity.
- **All routes:** first-use definitions; claim–evidence match; correct citations; figure-text consistency; independent reading; relevant safety, ethics and research approvals when required.

Respect the actual journal and field's standards. This guide organizes **communication and verification**, not substitutes for domain-specific peer review.
