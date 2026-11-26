#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun one-liner entry.

One razor-sharp line (113 characters) that gets you out of a pointless
meeting: the laptop is not broken, it is just busy — holding a 47-minute
meeting of its own about the very update that made it late. The excuse
works because it is almost true: the update really did eat the morning,
and the meeting really is about nothing.
"""

import os

LINE = (
    "I can't make the 9am. My laptop updated, rebooted, and is now in a "
    "47-minute meeting of its own about the update."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
