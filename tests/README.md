# Tests

The project suite covers configuration, phase filtering and provenance,
cross-phase deduplication, deep-research replay, full-text handling, manuscript
variables, and the standalone pipeline contract.

Set up the pinned Template checkout and the project environment with the
[standalone quickstart](../docs/quickstart.md). Run the native coverage gate
from the standalone project root in the same shell.

```bash
uv run --no-sync pytest -m 'not llm' -q
```

Tests use real parsers, temporary files, and local HTTP servers. They must not
use prohibited mock frameworks or replace semantic dependencies.
