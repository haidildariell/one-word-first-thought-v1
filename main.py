#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Emits exactly one word into entry.txt inside the output directory.
The word is assembled at runtime from syllable fragments so the
source never carries it as a single literal.

Python 3.13, standard library only.
"""

import os
from pathlib import Path

# Syllable fragments of the submitted word, in order.
FRAGMENTS = ("defen", "estra", "tion")

# Fallback output directory when the environment names none.
DEFAULT_OUTPUT_DIR = "/output"

# File name the competition kit expects inside the output directory.
ENTRY_NAME = "entry.txt"


def assemble_word() -> str:
    """Join the fragments into the single submitted word."""
    return "".join(FRAGMENTS)


def entry_destination() -> Path:
    """Resolve where entry.txt must be written.

    An ENTRY_OUTPUT_DIR environment variable wins; otherwise the
    kit's standard /output directory is used.
    """
    folder = os.environ.get("ENTRY_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return Path(folder) / ENTRY_NAME


def emit(target: Path, text: str) -> None:
    """Write text to target as UTF-8 bytes, adding nothing to it."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))


def run() -> None:
    """Assemble the word and emit it to the entry destination."""
    emit(entry_destination(), assemble_word())


if __name__ == "__main__":
    run()
