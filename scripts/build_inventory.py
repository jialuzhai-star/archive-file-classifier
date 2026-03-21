#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recursively build a file inventory CSV for archive classification."
    )
    parser.add_argument("target", help="Target directory to scan")
    parser.add_argument("--output", required=True, help="Output CSV path")
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden files and folders",
    )
    return parser.parse_args()


def is_hidden(path: Path) -> bool:
    return any(part.startswith(".") for part in path.parts)


def scan_files(target: Path, include_hidden: bool):
    for path in sorted(target.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(target)
        if not include_hidden and is_hidden(rel):
            continue
        stat = path.stat()
        yield {
            "relative_path": rel.as_posix(),
            "file_name": path.name,
            "extension": path.suffix.lower(),
            "parent_dir": rel.parent.as_posix() if rel.parent != Path(".") else "",
            "size_bytes": stat.st_size,
            "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
        }


def main() -> int:
    args = parse_args()
    target = Path(args.target).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()

    if not target.exists() or not target.is_dir():
        raise SystemExit(f"Target directory does not exist or is not a directory: {target}")

    output.parent.mkdir(parents=True, exist_ok=True)

    rows = list(scan_files(target, include_hidden=args.include_hidden))
    with output.open("w", newline="", encoding="utf-8-sig") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=[
                "relative_path",
                "file_name",
                "extension",
                "parent_dir",
                "size_bytes",
                "modified_at",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Scanned {len(rows)} files")
    print(f"Inventory written to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
