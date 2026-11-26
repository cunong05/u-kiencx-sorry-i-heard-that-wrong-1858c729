#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun bounty entry.

Writes the single-line apology to /output/entry.txt (no trailing newline)
and prints it. Deterministic: the text is fixed.
"""

from pathlib import Path

ENTRY = (
    "Sorry, I heard 'play jazz' as 'order twelve pizzas.' "
    "They're on their way, and frankly, they sound better than jazz."
)

# Gate limits from the bounty rules: the entry must be 1–140 characters
# of UTF-8 text, a single line, and not only whitespace.
MIN_ENTRY_LEN = 1
MAX_ENTRY_LEN = 140


def main() -> None:
    if not MIN_ENTRY_LEN <= len(ENTRY) <= MAX_ENTRY_LEN:
        raise ValueError(
            f"entry must be {MIN_ENTRY_LEN}-{MAX_ENTRY_LEN} characters, "
            f"got {len(ENTRY)}"
        )
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")

    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
