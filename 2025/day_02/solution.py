from typing import TextIO
from pathlib import Path
import math

DIAL_SIZE = 100
START = 50
FILE = Path("files/input.txt")


def is_repeated_twice(n: int) -> bool:
    s = str(n)
    half = len(s) // 2
    return len(s) % 2 == 0 and s[0:half] == s[half:]


def is_repeated_at_least_twice(n: int) -> bool:
    s = str(n)

    for i in range(len(s) // 2):
        window = s[0 : i + 1]

        # Can't make a window of this size and have it repeat.
        if len(s) % len(window) != 0:
            continue

        for j in range(0, len(s) // len(window) - 1):
            next_window = s[(j + 1) * len(window) : (j + 2) * len(window)]
            if next_window != window:
                break
        else:
            return True

    return False


def main() -> None:
    part_1 = 0
    part_2 = 0
    for p in FILE.read_text(encoding="utf-8").strip().split(","):
        start, end = [int(d) for d in p.split("-")]
        for i in range(start, end + 1):
            if is_repeated_twice(i):
                part_1 += i
            if is_repeated_at_least_twice(i):
                part_2 += i

    pairs = tuple(
        tuple(map(int, p.split("-")))
        for p in FILE.read_text(encoding="utf-8").strip().split(",")
    )

    print(f"Part 1: {part_1}")
    print(f"Part 1: {part_2}")
    assert part_1 == 64215794229
    assert part_2 == 85513235135


if __name__ == "__main__":
    main()
