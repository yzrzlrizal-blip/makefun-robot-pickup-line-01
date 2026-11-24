"""The Robot Pickup Line Championship.

Writes a single robot pickup line to /output/entry.txt. The line is
fixed and deterministic: the same line every run, so the entry is
reproducible and the gate (1-200 UTF-8 characters, not only
whitespace) always passes.
"""

from pathlib import Path

LINE = (
    "I ran a million simulations of this moment, and in every single "
    "one, you say yes."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate refuses any text outside 1-200 characters, so refuse
    # to write an over-long line rather than submit an invalid entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line is {len(LINE)} characters; gate allows 1-200")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
