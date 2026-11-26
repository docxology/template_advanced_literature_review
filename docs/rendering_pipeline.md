# Rebuild the manuscript from the synthetic corpus

Install Git, uv, Pandoc 3.14 with pandoc-crossref 0.3.26b, and XeLaTeX with the
[required TeX packages](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/usage/output-formats.md).
Use a spare checkout because the preparation steps regenerate files under
`output/`, which also holds the versioned evidence snapshot.

From a clean checkout of this repository:

```sh
set -e
project_root="$(pwd -P)"
renderer="$(mktemp -d)/template"
git clone https://github.com/docxology/template.git "$renderer"
git -C "$renderer" checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
mkdir -p "$renderer/projects/working"
project_copy="$renderer/projects/working/template_advanced_literature_review"
git clone --no-hardlinks "$project_root" "$project_copy"
git -C "$project_copy" checkout --detach "$(git -C "$project_root" rev-parse HEAD)"
cd "$renderer"
uv sync --locked --no-dev

cd "$project_copy"
uv sync --locked --python 3.13 --extra dev
export PYTHONPATH="$renderer${PYTHONPATH:+:$PYTHONPATH}"
export MPLBACKEND=Agg
# Remove prior generated figures from the disposable build copy.
find output/figures -maxdepth 1 -type f -name '*.png' -delete
rm -f output/figures/figure_registry.json
uv run --no-sync python scripts/01b_fixture_phase_replay.py
uv run --no-sync python scripts/02_meta_analysis_pipeline.py
uv run --no-sync python scripts/04_generate_figures.py --dpi 300
uv run --no-sync python scripts/06_fulltext_assessment.py
uv run --no-sync python scripts/07_literature_evaluation.py --fixture-honesty
uv run --no-sync python scripts/08_deep_research_dispatch.py
uv run --no-sync python scripts/09_export_bibliography.py
uv run --no-sync python scripts/05_inject_variables.py

cd "$renderer"
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/template_advanced_literature_review --skip-manuscript-hydration
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/template_advanced_literature_review
```

Stage 03 uses the manuscript already hydrated by the project’s step 05.
Find the combined PDF in `output/pdf/`, the HTML index at
`output/web/index.html`, and validation reports and provenance under
`output/reports/` in the disposable project copy. Authored Markdown and its
methodological bibliography remain in [manuscript/](manuscript/README.md).
The exported corpus bibliography under `output/data/` serves a separate
purpose.

The offline workflow uses the tracked synthetic corpus and local replay
fixture. Live retrieval, model-backed filtering and extraction, full-text
downloads, and reproducibility scoring are optional workflows outside this
build. A fork can configure those workflows in
[config.yaml](manuscript/config.yaml).
