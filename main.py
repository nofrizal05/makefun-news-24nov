#!/usr/bin/env python3
"""The World in One Day — 24 November 2026.

make.fun entry for news-image-20261124: "Sum up 24 November's world
news in one image". The finished front page ships with this entry as
entry.png (a 1024x1024 PNG drawn for this day's news); this program
simply places a copy of it in the grading output directory.

The front page leads with Jensen Huang's return as Nvidia CEO — shares
up more than 30%, Nasdaq +6.5% — followed by five panels: 24 dead in
the Banten candy factory fire, the Russian cargo ship Sparta II ablaze
in the Gulf of Finland, fresh strikes on Ukraine's Kyiv region, Lisbon
marching over the cost of living, and Alcaraz winning the ATP Finals.
A footer strip carries the day's smaller headlines.

Only the Python standard library is used, because the grading sandbox
runs Python 3.13 with nothing else installed.
"""

import os
import shutil
from pathlib import Path

# The image that ships alongside this script.
SOURCE_IMAGE = Path(__file__).resolve().parent / "entry.png"

# Where the grader expects the finished image. The harness sets
# MAKEFUN_OUTPUT_DIR; falling back to a local "output" folder keeps
# the script runnable by hand for a quick local check.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))


def main():
    """Copy the front-page image into the output directory."""
    if not SOURCE_IMAGE.is_file():
        raise SystemExit(f"Missing shipped image: {SOURCE_IMAGE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE_IMAGE, target)
    size = target.stat().st_size
    if size >= 1024 * 1024:
        raise SystemExit(f"Output image too large: {size} bytes")
    print(f"Wrote {target} ({size} bytes)")


if __name__ == "__main__":
    main()
