# Quick start

From the standalone project root, install Git, uv, and Python 3.11 or later.
The tested commands select Python 3.13 and install the committed dependency
versions, including the native test tools.

```sh
uv sync --locked --python 3.13 --extra dev
uv run --no-sync pytest -m 'not llm' -q
```

The configured 90% branch-coverage gate measures the project-owned
`src/multi_phase/` modules. The fixture can be replayed locally:

```sh
uv run --no-sync python scripts/01b_fixture_phase_replay.py
uv run --no-sync python scripts/02_meta_analysis_pipeline.py
```

Fixture replay reads the tracked `output/data/corpus.jsonl` and writes
phase corpora, membership, and provenance under `output/data/`. It does not
contact retrieval or model providers. Use a disposable checkout to keep the
committed output snapshot available for comparison.

[Configuration](manuscript/config.yaml) defines the topic, phase order,
queries, integration policy, and manuscript metadata. The complete
[build and validation procedure](rendering_pipeline.md) also rebuilds figures,
assessment reports, and the manuscript.
