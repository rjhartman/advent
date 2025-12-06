from pathlib import Path
from typing import List, Tuple

REAL_FILE = Path("files/input.txt")
TEST_FILE = Path("files/test.txt")

Range = Tuple[int, int]


def parse(file: Path) -> Tuple[List[Range], List[int]]:
    ranges = []
    numbers = []
    end_ranges = False
    for line in (l.strip() for l in file.read_text().strip().splitlines()):
        if not line:
            end_ranges = True
            continue
        if end_ranges:
            numbers.append(int(line))
        else:
            ranges.append(tuple(int(x) for x in line.split("-", maxsplit=1)))
    return ranges, numbers


def is_spoiled(number: int, ranges: List[Range]) -> bool:
    return not any(number >= start and number <= end for start, end in ranges)


def part_1(ranges: List[Range], numbers: List[int]) -> int:
    total = 0
    for number in numbers:
        if not is_spoiled(number, ranges):
            total += 1

    return total


def part_2(ranges: List[Range]) -> int:
    ranges = sorted(ranges)
    last = ranges[0]
    total = last[1] - last[0] + 1
    for i in range(1, len(ranges)):
        start, end = ranges[i]
        if end <= last[1]:
            continue

        start = max(last[1] + 1, start)
        last = (start, end)
        total += end - start + 1

    return total


def main() -> None:
    test_ranges, test_numbers = parse(TEST_FILE)
    real_ranges, real_numbers = parse(REAL_FILE)

    ans_1 = part_1(test_ranges, test_numbers)
    ans_2 = part_2(test_ranges)
    print("====== TEST DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 3
    assert ans_2 == 14

    ans_1 = part_1(real_ranges, real_numbers)
    ans_2 = part_2(real_ranges)
    print("====== REAL DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 694
    assert ans_2 == 352716206375547


if __name__ == "__main__":
    main()
