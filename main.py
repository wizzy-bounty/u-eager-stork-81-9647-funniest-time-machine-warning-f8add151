"""Funniest Time Machine Warning Label.

Writes one warning label (77 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Python stdlib only, no network, deterministic.

Design: a deadpan safety notice whose punchline lands in the last words —
warning your past self is itself the paradox, and you already failed at it.
"""

import os

LABEL = "NOTICE: Do not warn yourself about this trip. You ignored you last time, too."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
