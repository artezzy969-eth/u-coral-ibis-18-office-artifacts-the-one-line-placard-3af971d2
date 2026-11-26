# Office Artifacts: The One-Line Placard Contest

A program that writes a single museum placard line for an ordinary office
object — the badge reader — treated as an ancient artifact.

## What it does

`main.py` writes one line (1–180 characters) to `entry.txt` in the output
directory: a dry, deadpan curator's label for a basalt badge reader from
c. 1100 BCE. It hummed for the worthy. The unworthy were never seen again.

## How to run it

```sh
python3 main.py
```

By default the line is written to `/output/entry.txt`. To choose another
output directory, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Python 3.13 standard library only; no network access, no dependencies.
The output is deterministic: every run writes the same bytes.
