# Retarget the review

Fork the standalone repository and edit the
[manuscript configuration](manuscript/config.yaml). The
[example configuration](manuscript/config.yaml.example) records the schema
without selecting an active topic. Review the following together:

- `project_config.search` sets the topic, baseline queries, and retrieval engines.
- `project_config.search_phases` sets the phase names, dependencies, queries,
  and filtering boundaries.
- `project_config.phase_integration` sets deduplication and cross-phase policy.
- `project_config.hypothesis_definitions` and `subfield_keywords` define the
  scoring and descriptive categories for the new topic.
- `paper`, `authors`, and `publication` identify the fork and its metadata.

The shipped corpus only exercises the shipped example. Supply a reviewed
snapshot with provenance for the new topic or deliberately run live retrieval.
Cross-phase overlap and citation sufficiency describe the configured method.
They do not establish empirical support for the topic's hypotheses.

Run the [native tests](quickstart.md) and
[offline build](rendering_pipeline.md) after changing the configuration.
Change related sections and citations under [manuscript/](manuscript/README.md)
and use the generated reports when inspecting new corpus-derived claims.

## Full-text download and reproducibility scoring

The optional enrichment workflow needs a configured full-text source and
provider. From a disposable checkout registered with the pinned renderer,
run the three scripts in dependency order:

```sh
uv run --no-sync python scripts/11_fulltext_download.py
uv run --no-sync python scripts/10_reproducibility_assessment.py
uv run --no-sync python scripts/05_inject_variables.py
```

Preserve the retrieval and scoring provenance for this run. Keep the new
evidence distinct from the bundled synthetic corpus replay.
