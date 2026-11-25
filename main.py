#!/usr/bin/env python3
"""Entry program for Everyday Things, Two Lines, Longer Run.

Writes a two-line entry (at most 400 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
an analogy that explains an everyday thing, and the honest
second line that admits what the analogy leaves out. The thing
is the snooze button, and the analogy is a loan.
"""

import os

TEXT = (
    "A snooze button is a small loan you take from your "
    "future self, in units of nine minutes.\n"
    "The interest is paid in panic, and your future self "
    "never agreed to the terms."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
