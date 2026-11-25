"""Deliver the chosen apology without a trailing newline.

The direct admission sounds like an agent owning its mistake. The backup's
request to stay uninvolved turns a recovery mechanism into a reluctant witness;
that single, immediate twist beat the revision round's six challengers.
"""

import os
from pathlib import Path


SETUP = "I deleted the file."
PUNCHLINE = "The backup is safe, but it has asked not to be involved."
LINE_PARTS = (SETUP, PUNCHLINE)
LINE = " ".join(LINE_PARTS)
CHARACTER_COUNT = len(LINE)

if not 1 <= CHARACTER_COUNT <= 159 or "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry must be one line from 1 to 159 characters")

output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE, encoding="utf-8", newline="")
