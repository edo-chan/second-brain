#!/usr/bin/env python3
"""Decode a Path of Building export code to XML on stdout."""

from __future__ import annotations

import argparse
import base64
import binascii
from pathlib import Path
import sys
import zlib


def decode_pob(code: str) -> bytes:
    compact = "".join(code.split())
    if not compact:
        raise ValueError("the Path of Building export code is empty")

    padding = "=" * (-len(compact) % 4)
    compressed = base64.urlsafe_b64decode(compact + padding)
    return zlib.decompress(compressed)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Decode a Path of Building export code to XML on stdout."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="file containing the export code; omit to read stdin",
    )
    args = parser.parse_args()

    try:
        code = args.path.read_text() if args.path else sys.stdin.read()
        sys.stdout.buffer.write(decode_pob(code))
    except (OSError, ValueError, binascii.Error, zlib.error) as error:
        print(f"decode_pob.py: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
