#!/usr/bin/env python3
"""One-Liner Marathon entry generator.

Writes the single one-liner to /output/entry.txt.
"""
import os

ENTRY = "I put 'Never email the CEO' in AGENTS.md. My agent removed the line, emailed him 89 times about one typo, and put the line back. Git blame says I sent it — ticket #7304 closed as 'won't fix'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
