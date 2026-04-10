# Python Standards

Use this reference when a Python task needs a sharper implementation or review checklist.

## Design Heuristics

- Prefer obvious control flow over clever compression.
- Keep data models explicit. Favor dataclasses or small typed containers over anonymous dictionaries when structure matters.
- Pass dependencies explicitly when doing so improves tests or clarity; do not add indirection without a concrete need.
- Treat filesystem and subprocess boundaries as failure points. Validate inputs and surface actionable errors.
- Preserve backward-compatible CLI behavior unless the task explicitly changes it.

## Review Checklist

- Does the change keep behavior local, or has it introduced unnecessary coupling?
- Are names specific enough that a reader can infer intent without tracing every call site?
- Are edge cases and invalid inputs handled where they enter the system?
- Are errors phrased so a user can recover?
- Is the test suite covering both success and failure paths that matter?
- Does the patch update docs or examples when config, CLI, or packaging behavior changes?

## Typing Guidance

- Add return annotations on non-trivial functions.
- Use concrete built-in generics such as `list[str]` and `dict[str, str]`.
- Avoid type aliases or protocols unless they simplify a real repeated pattern.
- Do not add heavyweight static typing ceremony to a small module just to satisfy style preferences.

## Formatting and Linting

Use Ruff as the single default tool for formatting and linting in this repository.

```bash
ruff format .
ruff check .
```

Prefer changing code to satisfy the rules over adding ignores. If an ignore is necessary, keep it local and explain the reason.

## Testing Strategy

- Start with the most targeted test or command that exercises the changed behavior.
- Finish with repository-level verification when the change is ready.
- Favor deterministic tests with minimal mocking.
- Test user-facing commands through the CLI surface when practical.
- Add regression tests for bug fixes before or alongside the fix.

Repository baseline:

```bash
pytest
python -m build
```

## Documentation Sync

Update repository guidance when developer workflow changes:

- `AGENTS.md` for contributor and agent workflow
- `README.md` for user-visible setup or command changes
- Example configuration under `examples/` when config fields or behavior change
