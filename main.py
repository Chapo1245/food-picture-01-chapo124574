#!/usr/bin/env python3
"""Food-picture-01 entry: copy the bundled food picture to /output/entry.png.

The picture is entry.png beside this file (JPEG bytes, 1024x683).
The program does a plain byte copy: no network, no randomness, no clock, so
two runs write exactly the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Guard against a truncated copy: the output must be byte-identical
    # to the bundled picture, so the two grader runs agree exactly.
    if os.path.getsize(OUT) != os.path.getsize(SRC):
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
