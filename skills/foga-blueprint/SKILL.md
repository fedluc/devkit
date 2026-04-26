---
name: foga-blueprint
description: Draft, review, or update `foga.yml` workflow blueprints for a repository. Use when Codex should inspect an existing project, identify its real build, test, docs, format, lint, install, or deploy workflows, map them to supported foga backends, and produce a validated configuration without assuming the foga source tree is present.
---

# Foga Blueprint

Use this skill to translate an existing repository's workflows into a working
`foga.yml`.

## Source of Truth

First determine where the skill is running.

### Inside the foga repository

When the local checkout contains the foga implementation and docs, treat that
checkout as authoritative for the current schema, supported backends, examples,
and CLI behavior. Use the local code, local documentation, examples, and CLI
help before relying on published documentation, because the checkout may include
unreleased changes.

### Outside the foga repository

When the foga source tree is not available, do not assume repo-local files or
examples exist. Treat the published documentation as the schema and behavior
source of truth:

https://fedluc.github.io/foga/

Use the installed `foga` CLI, when present, to validate and inspect the file you
produce. If neither the published docs nor the CLI are available, explain that
the config is a best-effort draft and identify the fields that need verification.

## Supported Backends

Check whether the target repository already uses any supported backend, and how
that workflow is invoked before adding it to `foga.yml`.

- Build: `cmake`, `meson`, `python-build`
- Test: `ctest`, `pytest`, `tox`
- Docs: `doxygen`, `mkdocs`, `sphinx`
- Format: `black`, `clang-format`, `ruff-format`
- Lint: `clang-tidy`, `pylint`, `ruff-check`
- Install: `apt-get`, `brew`, `npm`, `pip`, `poetry`, `uv`, `yum`
- Deploy: `twine`

## Workflow

1. Inspect the target repository's existing build, test, documentation,
   formatting, linting, installation, deployment, CI, and release workflows
   before writing config.
2. Identify the real commands users already rely on. Keep separate workflows
   separate when the repository treats them separately.
3. Map each workflow to the narrowest supported foga backend that preserves the
   behavior. Do not infer a backend from language or project type alone.
4. Use built-in backend fields for normal arguments, paths, environment, and
   launchers. Add hooks only for small project-specific setup or cleanup that a
   backend cannot express directly.
5. Add profiles only for real environment variants, such as platform-specific
   settings, local versus CI behavior, release mode, or optional feature sets.
6. Validate and inspect the generated config with the available foga CLI before
   finishing whenever possible.

## Authoring Rules

- Prefer a small base config that users can run immediately; add optional
  workflows after the base build and test path is clear.
- Keep paths relative to the repository root that will contain `foga.yml`.
- Choose the backend that represents the behavior users rely on, not merely a
  wrapper command. Preserve wrappers when they provide isolation, environment
  setup, matrix behavior, or a documented entry point.
- For native builds and tests, model the actual sequence the project uses. If a
  test workflow needs a build or configure step first, include only that
  prerequisite work; if it assumes an existing build tree, keep the test runner
  minimal.
- Use explicit build targets only when the repository has stable named targets
  that users select intentionally.
- Keep environment variables close to the workflow that needs them. Use profiles
  when values vary by mode rather than by workflow type.
- Do not encode full bootstrap or dependency installation flows in hooks when
  the target environment already handles them.

## Validation

- Run `foga validate` against the generated file when the CLI is available.
- Run `foga inspect` to confirm the resolved configuration and profile merges.
- Use dry-run commands for the workflows you configured when the CLI supports
  them.
- Explain any remaining assumptions, such as external system packages,
  credentials, platform-specific tools, or workflows that could not be verified
  locally.
