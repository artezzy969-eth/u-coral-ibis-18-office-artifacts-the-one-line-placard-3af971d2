#!/usr/bin/env python3
"""Write the one-line museum placard for the Office Artifacts contest.

The program is deterministic: it always writes the same single placard
line to ``entry.txt`` inside the output directory given by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``).
"""

import os
from pathlib import Path

PLACARD_LINE = (
    "Badge Reader, basalt, c. 1100 BCE. "
    "It hummed for the worthy. The unworthy were never seen again. "
    "Gift of Security."
)


def write_entry(output_dir: Path) -> Path:
    """Write the placard line to ``entry.txt`` in ``output_dir``."""
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(PLACARD_LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(output_dir)


if __name__ == "__main__":
    main()
