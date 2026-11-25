#!/usr/bin/env python3
"""Write one original crypto-trading joke line to /output/entry.txt."""

import os

JOKE = (
    "I bought the dip, the dip dipped again, and now I tell people "
    "I'm a long-term investor — the group chat has screenshots."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
