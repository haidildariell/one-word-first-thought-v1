#!/usr/bin/env python3
"""One Word, First Thought — writes the single word 'defenestration'."""

import os
from pathlib import Path

WORD = "defenestration"


def output_path() -> Path:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
