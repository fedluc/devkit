"""Helpers for the ``foga docs`` command."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated

import typer

from ..adapters.docs import plan_docs
from ..config.loading import load_config
from ..config.models import FogaConfig
from ..errors import ConfigError
from ..executor import CommandExecutor
from .common import config_path_from_context, select_named_items


@dataclass(slots=True)
class DocsArgs:
    """Parsed arguments for the docs command."""

    targets: list[str] | None
    dry_run: bool


def docs_command(
    ctx: typer.Context,
    profile: Annotated[
        str | None,
        typer.Option(
            "--profile",
            help="Apply a named configuration profile before resolving the command.",
        ),
    ] = None,
    targets: Annotated[
        list[str] | None,
        typer.Option(
            "--target",
            help="Run only the named docs target. Repeat to select multiple targets.",
        ),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            help="Show the planned docs commands without executing them.",
        ),
    ] = False,
) -> int:
    """Run configured documentation workflows."""

    config = load_config(config_path_from_context(ctx), profile)
    executor = CommandExecutor(config.project_root)
    args = DocsArgs(targets=targets, dry_run=dry_run)
    return run_docs(config, executor, args)


def run_docs(config: FogaConfig, executor: CommandExecutor, args: DocsArgs) -> int:
    """Execute configured documentation workflows."""

    selected = select_named_items(config.docs.targets, args.targets, "docs target")
    plan = plan_docs(config.project_root, list(selected.values()))
    if not plan.specs:
        raise ConfigError("No docs workflows configured")
    executor.run_specs(plan.specs, dry_run=args.dry_run)
    return 0
