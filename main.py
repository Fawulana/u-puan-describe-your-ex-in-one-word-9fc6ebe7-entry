"""Describe Your Ex in One Word — entry program.

Writes exactly one word to /output/entry.txt: the verdict on the ex.
Standard library only, deterministic, offline. Every run produces the
same bytes.
"""

import os
from pathlib import Path

# The whole entry: one word, no punctuation, no caption needed.
# A placeholder is the thing that occupies a spot only until the real
# one arrives — which is, in hindsight, exactly what the ex was.
WORD = "Placeholder"

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    out_path = Path(os.environ.get("ENTRY_OUTPUT_PATH", DEFAULT_OUTPUT))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Write raw UTF-8 bytes so the file holds the word and nothing else:
    # no trailing newline, no platform line-ending translation.
    out_path.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
