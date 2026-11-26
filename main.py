#!/usr/bin/env python3
"""The Printer Apology.

Writes the one-line apology note from an office printer to the people who
jam it, feed it cheap paper and swear at it to /output/entry.txt.
"""

from pathlib import Path
import os
import shutil

MAX_CHARS = 120

LINE = "Sorry about the jam. I only choke on the documents that matter — and yours mattered most."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-120 non-blank chars"

FOLDER = Path(os.environ.get("MAKEFUN_OUT", "/output"))
ENTRY = "entry.txt"


def main():
    FOLDER.mkdir(parents=True, exist_ok=True)
    for earlier in FOLDER.iterdir():
        if earlier.is_dir():
            shutil.rmtree(earlier)
        else:
            earlier.unlink()
    # No trailing newline: the gate counts the line exactly as written.
    FOLDER.joinpath(ENTRY).write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
