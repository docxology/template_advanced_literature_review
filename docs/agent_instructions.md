# AI Agent Instructions - Advanced Literature Review Exemplar

Read this before modifying `template_advanced_literature_review`. See also the
project root [`AGENTS.md`](../AGENTS.md), which this file specializes for
`docs/`-adjacent work.

## Rule 1: Config Owns Phase Design and Domain Policy

`docs/manuscript/config.yaml` → `project_config.search_phases` is the control
surface for how many phases exist, their queries, engines, and temporal
filters. `llm_filters`, `phase_integration`, and `hypothesis_definitions`
control content filtering and cross-phase policy. Retargeting to a new domain
or phase design should primarily be a config change — see `forking_guide.md`.

## Rule 2: Scripts Stay Thin, Numbered By Dependency Order

`scripts/01_multi_phase_search.py` through `scripts/11_validate_outputs.py`
orchestrate stage inputs, outputs, logging, and CLI flags only. Business
logic — phase search, filtering, provenance, bibliometrics, embeddings,
hypothesis scoring, figure generation, token computation — lives in `src/`.
Two scripts share the `11_` prefix (`11_fulltext_download.py`,
`11_validate_outputs.py`) by design, not error; `AGENTS.md` → "Regeneration
Order" documents that `11_fulltext_download.py` must run before
`10_reproducibility_assessment.py`, ahead of `11_validate_outputs.py`.

## Rule 3: Standalone Module Ownership

The analysis, knowledge-graph, reproducibility, and visualization modules and
`src/config_loader.py` are regular files in this checkout. Coordinate
changes to shared behavior with the single-term exemplar.

## Rule 4: No Mocks

Tests use real objects, real temporary files, and local HTTP servers through
`pytest-httpserver`. Do not add `unittest.mock`, `MagicMock`,
`mocker.patch`, or call-count-only assertions.

## Rule 5: Tracked Corpus Snapshot Honesty

The committed per-phase corpora and `output/data/combined_corpus.jsonl` are a
tracked evidence snapshot. They demonstrate the pipeline; they are not a live
empirical claim about exoplanet atmospheric research. Real claims require
running `scripts/01_multi_phase_search.py` live and regenerating downstream
artifacts.

## Rule 6: Output Is Disposable

Never hand-edit `output/`, including `phase_metadata.json` or any
`phase_*_corpus.jsonl`. To change generated manuscript text, edit source
manuscript sections, config, or `src/manuscript/variables/` and rerun
`scripts/05_inject_variables.py`. To change phase results, edit the relevant
`src/multi_phase/` or `src/literature/` producer and rerun stage 01.

## Rule 7: Use Generated Facts

Live counts and coverage snapshots belong in
`../../../../docs/_generated/COUNTS.md`. Public exemplar membership belongs
in `../../../../docs/_generated/active_projects.md` and
`../../../../docs/_generated/exemplar_roster.md`.

## Rule 8: Preserve Phase Provenance

Every generated artifact that depends on the corpus should be traceable back
to the phase(s) that contributed its data — `phase_metadata.json` is the
source of truth. Do not add a new pipeline stage that drops phase attribution
silently; see the [historical backlog](archive/TODO.md)
for the original phase provenance follow-up.

## Rule 9: Verify the touched surface

Use the [native test command](quickstart.md) and the
[pinned manuscript build](rendering_pipeline.md).
