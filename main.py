"""One Word for the Boss — entry program.

Writes exactly one word describing the boss to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The word: "Unfireable" — the boss who can never be fired, no matter
what. Funny on its own, true of bosses everywhere, and fresh next to
the usual "micromanager".
"""

import os

WORD = "Unfireable"

# Gate from RULES.txt: entry.txt must be UTF-8 text of 1 to 30
# characters, not only white space — and the judge's first criterion
# is that it is exactly one word, no spaces, no sentence.
MIN_LEN = 1
MAX_LEN = 30


def validate(word: str) -> None:
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        raise ValueError(f"word must be {MIN_LEN}-{MAX_LEN} chars, got {len(word)}")
    if not word.strip() or word != word.strip():
        raise ValueError("word must not be blank or padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
