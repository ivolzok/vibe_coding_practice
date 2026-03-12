from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image


ASCII_CHARS = "@%#*+=-:. "
TARGET_WIDTH = 100
TARGET_HEIGHT = 50


def image_to_ascii(image_path: Path, width: int = TARGET_WIDTH, height: int = TARGET_HEIGHT) -> str:
    if not image_path.exists():
        raise FileNotFoundError(f"File not found: {image_path}")
    if not image_path.is_file():
        raise IsADirectoryError(f"Not a file: {image_path}")

    with Image.open(image_path) as img:
        img = img.convert("L")
        img = img.resize((width, height), Image.Resampling.LANCZOS)

        pixels = list(img.getdata())
        n = len(ASCII_CHARS)
        mapped = (ASCII_CHARS[p * n // 256] for p in pixels)

        lines = []
        row = []
        for i, ch in enumerate(mapped, start=1):
            row.append(ch)
            if i % width == 0:
                lines.append("".join(row))
                row.clear()

        return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art (100x50, grayscale).")
    parser.add_argument("image_path", type=Path, help="Path to input image (png/jpg/etc.)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        art = image_to_ascii(args.image_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    print(art)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
