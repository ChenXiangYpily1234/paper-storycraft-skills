# Citation and Reference Integrity Guide

> **Scope:** All STEM manuscripts revised with Paper StoryCraft. Read alongside [PRINCIPLES.md](PRINCIPLES.md). Follow the actual venue and manuscript citation system. This guide governs **manuscript citations**; the Skills repository itself is not a research paper requiring its own bibliography.

## 1. Source every imported research object

At the **first meaningful mention**, attribute externally sourced entities to verified original or authoritative sources, including those named only in tables, captions, appendices and figures.

| Object | Preferred source | Specific check |
| --- | --- | --- |
| Prior method, algorithm, system | Original paper; separate paper for a later extension | Do not misattribute subsequent work to its predecessor |
| Model, pretrained backbone, checkpoint | Primary model paper, technical report, official release | Distinguish model family, variant and fine-tuned checkpoint |
| Dataset or corpus | Original dataset paper or official documentation | Record version, split and preprocessing if they matter |
| Benchmark, shared task or evaluation suite | Benchmark paper or official protocol | Cite **both benchmark and constituent dataset** when sources differ |
| Imported metric, objective, tool, instrument or protocol | Original definition or authoritative software/protocol source when scientifically material | Distinguish protocol variants and avoid citing trivial mathematical notation |
| Reproduced result, adapted figure or table | Original result or resource | Mark external/adapted content clearly |

**Mandatory:** externally sourced **models, benchmarks and datasets need corresponding citations**. A paper using a dataset is not necessarily the paper that introduced it. A benchmark citation may not cover its underlying dataset; a model family citation may not document the exact evaluated checkpoint. For the author's own new/unpublished asset, state provenance rather than inventing a reference. If no paper exists, use verified official documentation or release information as allowed by the venue. Missing verification belongs in an explicit SOURCE NEEDED list, not in fabricated BibTeX.

## 2. Citation placement follows meaning, not sentence endings

Place the citation **immediately after the named entity** for provenance, or **next to the smallest claim** it supports for reported findings. Do **not** require citations at the end of every sentence.

Author–year formatting illustration: **“DistillM (Ko et al., 2024) ...”**. The quotation illustrates the user's desired citation **position**; confirm the bibliographic record independently before using it. Author-led alternatives such as “Ko et al. (2024) introduced DistillM ...” are also valid. If the next clause states a comparative gain or limitation, check that the citation supports that precise claim; entity attribution and experimental evidence are separate jobs.

Common LaTeX patterns (adapt to the actual document class/package):

| Citation setup | Name-first | Author-first |
| --- | --- | --- |
| natbib, author–year | MethodName~\citep{verified_key} | \citet{verified_key} introduced MethodName |
| biblatex, author–year | MethodName~\parencite{verified_key} | \textcite{verified_key} introduced MethodName |
| Numeric style | MethodName~\cite{verified_key} | Follow venue-supported narrative formatting |

Here **verified_key** is a placeholder, **not an actual reference**. Do not mix natbib and biblatex commands. Avoid placing a citation cluster only at paragraph end when different references establish different claims. Cite again when a later claim needs independent attribution, but do not attach a reference to every trivial repetition.

## 3. Entity–source ledger

Before rewriting, create and check this ledger:

| External entity or claim | Type | Exact version | First location (also tables/captions) | Source and which claim it supports | Existing verified key | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [real name] | model / dataset / benchmark / method / claim | [variant] | [section or float] | [primary paper, DOI or official page] | [key or unresolved] | verified / missing / mismatch |

Separate (a) **provenance** of an entity, (b) **evidence** for a result claimed about it, and (c) **implementation provenance** of a particular dataset split/model release. Review baseline model labels, dataset tables and benchmark charts that are often absent from prose.

## 4. References must exist and must support the text

1. Verify actual title, authors, year, venue, DOI/URL and relevant content against the original paper, proceedings, publisher, DOI record or official release. Prefer primary sources; distinguish preprint versions from published versions.
2. Reuse correct manuscript citation keys. Add entries only with validated metadata. Never invent papers, BibTeX, DOI, author names or years.
3. Match all in-text keys to real bibliography entries; check missing/duplicate entries, key collisions, year/author mismatches and stale references. Do not silently delete legitimate existing records.
4. Check the **reference list is actually generated**: the correct bibliography resource/path and the appropriate BibTeX/Biber/output commands or document-native equivalents. A visible in-text cite alone does not prove the References section exists.
5. When compilation assets are available, inspect undefined citation warnings and the rendered PDF References section. Without a build or bibliography, report **NOT CHECKED**, never PASS.
6. In lossless edits, preserve valid existing citations and add/relocate only verified sources; list changes and any unresolved citation requests.

## 5. Acceptance thresholds

**P0:** fabricated reference, critical misattribution, unsupported source-dependent claim, broken final reference list.

**P1:** missing external model/benchmark/dataset citation, wrong version, source separated from its entity or claim, missing citation in an independently read table/caption.

**P2:** non-substantive styling inconsistencies or redundant citations.

Report separate outcomes for **entity coverage**, **claim-to-source accuracy**, **bibliography/key integrity**, and **compiled References verification**. Presence of citation syntax is not evidence that the source is correct.
