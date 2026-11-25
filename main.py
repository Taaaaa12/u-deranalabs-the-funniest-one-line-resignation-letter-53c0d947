#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

Deterministic: the same single line on every run, no input, no network,
no randomness, no clock. Runs on python3.13.
"""

import os

LINE = (
    "I fired every minute since March, never missed once, and my "
    "performance review was a log line that said OK. I quit."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
