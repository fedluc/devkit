from __future__ import annotations

import os
import shlex
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from .errors import ExecutionError


@dataclass(frozen=True)
class CommandSpec:
    command: list[str]
    cwd: Path | None = None
    env: dict[str, str] = field(default_factory=dict)
    description: str | None = None


class CommandExecutor:
    def __init__(self, project_root: Path):
        self.project_root = project_root

    def run_specs(self, specs: list[CommandSpec], dry_run: bool = False) -> None:
        for spec in specs:
            self.run(spec, dry_run=dry_run)

    def run(self, spec: CommandSpec, dry_run: bool = False) -> None:
        command_str = shlex.join(spec.command)
        prefix = "[dry-run]" if dry_run else "[run]"
        suffix = f" ({spec.description})" if spec.description else ""
        print(f"{prefix} {command_str}{suffix}")
        if dry_run:
            return

        env = os.environ.copy()
        env.update(spec.env)
        try:
            subprocess.run(
                spec.command,
                cwd=spec.cwd or self.project_root,
                env=env,
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise ExecutionError(f"Command failed: {command_str}") from exc
