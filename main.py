#!/usr/bin/env python3
"""One Letter for Your Day — entry: the letter Z.

Z stands for "zero sleep": a day so exhausting it ends at the last
letter of the alphabet. Writes exactly one byte, "Z", to
/output/entry.txt, with no trailing newline.
"""

import os

LETTER = "Z"


def main() -> None:
    # Guard: the entry must be exactly one uppercase ASCII letter.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", LETTER
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Re-read and verify the written bytes before exiting.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == LETTER.encode("ascii")


if __name__ == "__main__":
    main()
