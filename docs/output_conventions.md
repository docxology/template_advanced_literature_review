# Output conventions

The tracked `output/` tree is the exemplar's versioned evidence snapshot.
The offline build replays the synthetic `output/data/corpus.jsonl` in a
disposable checkout and regenerates derived outputs. Change producers or
authored inputs to update artifacts.

| Location | Contents |
| --- | --- |
| `output/data/` | Fixture corpus, phase membership, computed analyses, and corpus bibliography |
| `output/figures/` | Analysis images and the figure registry |
| `output/manuscript/` | Hydrated Markdown and runtime config used for rendering |
| `output/pdf/`, `output/web/` | Combined PDF and HTML editions |
| `output/reports/` | Validation, evidence registry, and rendered provenance |

The [inventory](output_inventory.md) lists the producers. The
[offline build guide](rendering_pipeline.md) gives their order. Live retrieval
and full-text enrichment are separate workflows with their own provenance.
