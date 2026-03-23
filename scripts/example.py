#!/usr/bin/env python3
"""Compatibility wrapper for archive-file-classifier.

Keep this file only because the initializer created it.
Route execution to build_inventory.py so the directory contains no misleading placeholder logic.
"""

from build_inventory import main

if __name__ == "__main__":
    raise SystemExit(main())
