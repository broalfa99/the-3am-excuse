#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign a transaction at 3 AM.

Entry for the make.fun bounty "The 3 AM Excuse"
(https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878).

The program writes a single line (under 200 characters) to /output/entry.txt:
the excuse, in the wallet's own voice. A vault's job is protection — and at
3 AM the thing it protects the coins from is its own owner.
"""

import os

LINE = "I kept your coins safe through three bear markets. At 3 AM, I keep them safe from you."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
