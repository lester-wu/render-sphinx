"""Command-line interface helpers."""
# Standard library
import argparse
import pathlib


def to_path(path: str) -> pathlib.Path:
    """Return a Path object from a path string."""
    return pathlib.Path(path)


class CLIParser(argparse.ArgumentParser):
    """Wrapper class for ArgumentParser to simplify parsing configuration."""

    def add_paths_arg(self) -> None:
        """Add a list type `paths` argument to the parser."""
        self.add_argument("paths", nargs="+", type=to_path)

    def add_positional_paths_arg(self) -> None:
        """Add a list type `paths` positional argument to the parser."""
        self.add_argument(
            "--paths", "-p", nargs="+", type=to_path, required=False
        )

    def add_run_kwarg(self) -> None:
        """Add a `run` keyword argument to the parser."""
        self.add_argument("--run", "-r", type=str, required=True)
