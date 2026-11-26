# FAQ

## What does the default corpus show?

It exercises the phase-aware retrieval, analysis, and rendering pipeline with
a synthetic exoplanet-atmosphere snapshot. Corpus counts and overlaps describe
this snapshot. Scientific conclusions require verified empirical data and an
appropriate review design.

## Why split the search into phases?

The example illustrates how separate query sets, date filters, and inclusion
criteria can be combined while retaining source attribution. The foundation,
JWST, and molecule phases are configured in
[config.yaml](manuscript/config.yaml) and can overlap. See the
[architecture](architecture.md) for the data flow.

## Where do I add phases, tokens, or figures?

Use the [retargeting guide](forking_guide.md) for a new phase or topic and the
[syntax guide](syntax_guide.md) for manuscript tokens and figures.

## Which outputs are tracked?

The repository keeps an [evidence snapshot](output_conventions.md).
Regenerate artifacts in a disposable checkout and inspect their provenance.
