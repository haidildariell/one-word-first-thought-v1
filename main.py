#!/usr/bin/env python3
"""One Word, First Thought — writes the single word 'defenestration'."""

import os
from pathlib import Path

_LETTER_GROUPS = ("de", "fen", "es", "tra", "tion")
_DEFAULT_DIR = "/output"
_ENTRY_NAME = "entry.txt"


def compose_entry_word() -> str:
    word = ""
    for group in _LETTER_GROUPS:
        word += group
    return word


def resolve_entry_file() -> Path:
    chosen = os.environ.get("ENTRY_OUTPUT_DIR") or _DEFAULT_DIR
    return Path(chosen).joinpath(_ENTRY_NAME)


def main() -> None:
    destination = resolve_entry_file()
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = compose_entry_word().encode("utf-8")
    with destination.open("wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()
