# SPDX-License-Identifier: MIT
"""Write the one-word verdict on an ex to /output/entry.txt.

Deterministic, offline, stdlib-only: the word is a fixed string, so every
run writes byte-identical output.
"""

import os

WORD = "Unsubscribe"
# The word is 11 characters: inside the 111-character cap, exactly one word, no punctuation.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
