# docs/ - Agent-Facing Documentation Hub

This directory documents how to work on the `template_advanced_literature_review` exemplar — the multi-phase sibling of `template_literature_meta_analysis`. Keep these files project-specific; do not copy single-term or private-sidecar wording into this public template.

## File Inventory

| File | Purpose |
| --- | --- |
| `README.md` | Quick navigation and canonical commands |
| `agent_instructions.md` | Rules agents must read before source, test, config, or manuscript edits |
| `architecture.md` | Pipeline layers, mirrored and project-specific modules, and dependency direction |
| `testing_philosophy.md` | No-mocks testing policy and representative multi-phase test surfaces |
| `style_guide.md` | Source, script, doc, and error-message conventions |
| `syntax_guide.md` | Markdown, citations, figure refs, and phase-aware token syntax |
| `rendering_pipeline.md` | Manuscript hydration and render sequence across the 11-stage pipeline |
| `output_conventions.md` | What `output/` means and how to regenerate it |
| `output_inventory.md` | Producer/consumer inventory for every generated artifact, including per-phase corpora |
| `forking_guide.md` | Retargeting the exemplar to a new domain and a new phase design |
| `troubleshooting.md` | Common pipeline failures and fixes, including phase-specific failure modes |
| `quickstart.md` | First-run commands |
| `faq.md` | Recurring project questions |

## Standalone layout

The analysis, knowledge-graph, reproducibility, and visualization modules
are regular files. The canonical paper is in `manuscript/` beneath this
directory. See [the documentation index](README.md) for current commands.
