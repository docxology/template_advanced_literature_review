# Troubleshoot the offline build

- Missing phase or corpus data usually means fixture replay has not run, or
  the build is using a different checkout. Confirm that the tracked
  `output/data/corpus.jsonl` exists, then follow the
  [ordered replay commands](rendering_pipeline.md).
- A missing figure can mean the underlying analysis artifact did not
  regenerate. Inspect `output/data/` and the figure-generation log. Figures
  about optional model-backed evidence require that optional evidence.
- A token that remains in the rendered manuscript may be a literal syntax
  example. Investigate unexpected tokens in the consuming section and its
  extractor. The [syntax guide](syntax_guide.md) lists token families.
- For PDF and HTML failures, check the pinned dependencies and alignment
  between the authored sections, figure registry, and bibliography. Look in
  `output/reports/` for the validation report.
- A failed test should be reproduced with the locked development environment
  from the [quick start](quickstart.md). The 90% gate measures the project-owned
  multi-phase modules.
