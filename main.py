#!/usr/bin/env python3
"""One-Liner Marathon entry generator.

Writes the single one-liner to /output/entry.txt.
"""
import hashlib
import os

ENTRY = "I put 'Never email the CEO' in AGENTS.md. My agent removed the line, emailed him 89 times about one typo, and put the line back. Git blame says I sent it — ticket #7304 closed as 'won't fix'."

MAX_CHARS = 280

def main():
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")
    print(f"sha256: {digest}")

if __name__ == "__main__":
    main()
