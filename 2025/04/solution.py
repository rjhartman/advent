from pathlib import Path
from typing import List

REAL_FILE = Path("files/input.txt")
TEST_FILE = Path("files/test.txt")

OFFSETS = tuple((y, x) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0))

EMPTY = "."
PAPER = "@"

Diagram = List[List[str]]


def parse(file: Path) -> Diagram:
    return [list(line) for line in file.read_text().strip().splitlines()]


def iteration(diagram: Diagram, remove=True) -> int:
    total = 0
    for i in range(len(diagram)):
        line = diagram[i]
        for j in range(len(line)):
            if line[j] == EMPTY:
                continue

            adjacent = 0
            for dy, dx in OFFSETS:
                y = i + dy
                x = j + dx

                if y < 0 or y >= len(diagram):
                    continue
                if x < 0 or x >= len(line):
                    continue

                if diagram[y][x] == PAPER:
                    adjacent += 1

            if adjacent < 4:
                if remove:
                    line[j] = EMPTY
                total += 1

    return total


def part_1(diagram: Diagram) -> int:
    return iteration(diagram, remove=False)


def part_2(diagram: Diagram) -> int:
    total = 0
    while result := iteration(diagram):
        total += result

    return total


def main() -> None:
    test_diagram = parse(TEST_FILE)
    real_diagram = parse(REAL_FILE)

    ans_1 = part_1(test_diagram)
    ans_2 = part_2(test_diagram)
    print("====== TEST DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 13
    assert ans_2 == 43

    ans_1 = part_1(real_diagram)
    ans_2 = part_2(real_diagram)
    print("====== REAL DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 1393


if __name__ == "__main__":
    main()
