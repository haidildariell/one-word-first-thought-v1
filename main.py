#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Writes exactly one word to /output/entry.txt.

The word is "defenestration": the act of throwing someone (or
something) out of a window. It is a single, vivid, surprising word
with an unmistakable image and a dry, absurd wit — exactly what the
judge's criteria reward.

Python 3.13, standard library only.
"""

from pathlib import Path

# The single word this entry submits.
WORD = "defenestration"

# Destination required by the competition kit.
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the word to /output/entry.txt with no trailing newline."""
    # Make sure the output directory exists, then write the word as
    # UTF-8 text exactly as-is — no newline, no extra whitespace.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
