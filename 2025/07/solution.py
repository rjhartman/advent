from pathlib import Path
from functools import lru_cache

REAL_FILE = Path("files/input.txt")
TEST_FILE = Path("files/test.txt")

START = "S"
BEAM = "|"
SPLITTER = "^"


def part_1(file: Path) -> int:
    splits = 0
    lines = list(list(l) for l in file.read_text().strip().splitlines())

    for i in range(1, len(lines)):
        line = lines[i]
        previous_line = lines[i - 1]
        for j in range(len(line)):
            if previous_line[j] not in [START, BEAM]:
                continue

            if line[j] == SPLITTER:
                splits += 1
                line[j - 1] = BEAM
                line[j + 1] = BEAM
            else:
                line[j] = BEAM

    return splits


def part_2(file: Path) -> int:
    lines = list(list(l) for l in file.read_text().strip().splitlines())
    height = len(lines)

    @lru_cache()
    def search(x: int, y: int) -> int:
        # Base case, we're at the bottom
        if y == height:
            return 1

        if lines[y][x] == SPLITTER:
            left = search(x - 1, y)
            return left + search(x + 1, y)

        return search(x, y + 1)

    return search(lines[0].index(START), 1)


def main() -> None:
    ans_1 = part_1(TEST_FILE)
    ans_2 = part_2(TEST_FILE)
    print("====== TEST DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 21
    assert ans_2 == 40

    ans_1 = part_1(REAL_FILE)
    ans_2 = part_2(REAL_FILE)
    print("====== REAL DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 1675
    assert ans_2 == 187987920774390


if __name__ == "__main__":
    main()
