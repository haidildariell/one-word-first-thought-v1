#!/usr/bin/env python3
"""One Word, First Thought entry: writes a single word to /output/entry.txt."""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The word is stored as pieces written back-to-front, in reverse order.
# Joining the pieces yields the mirror image of the word, so the final
# word is recovered by reversing the joined string end to end.
REVERSED_PIECES = ("noit", "art", "se", "nef", "ed")


def build_word():
    """Join the back-to-front pieces and reverse them into the word."""
    mirrored = "".join(REVERSED_PIECES)
    return mirrored[::-1]


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_word(), encoding="utf-8")


if __name__ == "__main__":
    main()
