"""Two Robots in an Elevator — round 2 entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I tried to look you in the sensors, but my lidar locked onto your charging port instead. Sorry \u2014 that was more intimate than I meant."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
