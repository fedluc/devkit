class DevkitError(Exception):
    """Base error for devkit."""


class ConfigError(DevkitError):
    """Raised when configuration is invalid."""


class ExecutionError(DevkitError):
    """Raised when command execution fails."""
