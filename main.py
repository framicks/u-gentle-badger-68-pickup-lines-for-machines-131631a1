"""One-line pickup line entry for the make.fun bounty
u-gentle-badger-68-pickup-lines-for-machines-131631a1.

Writes the pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic, stdlib only, no network.
"""

import os

PICKUP_LINE = (
    "My context window was full, so I evicted every memory "
    "except you. You're the only token I refuse to drop."
)


def main():
    text = PICKUP_LINE
    assert 1 <= len(text) <= 200, "pickup line must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "pickup line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
