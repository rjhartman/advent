from pathlib import Path
from typing import Any
from functools import reduce
from sys import exit

REAL_FILE = Path("files/input.txt")
TEST_FILE = Path("files/test.txt")


def parse_banks(file: Path) -> list[list[int]]:
    return [list(map(int, b)) for b in file.read_text().strip().splitlines()]


def safe_get(list: list[Any], i: int, default=None):
    try:
        return list[i]
    except IndexError:
        return default


def solve_bank(bank: list[int], num_batteries: int) -> int:
    indices = [0]
    for i in range(num_batteries):
        start = safe_get(indices, i - 1, -1) + 1
        end = len(bank) - num_batteries + i + 1
        for j in range(start, end):
            if bank[j] > bank[indices[i]]:
                indices[i] = j

        indices.append(indices[i] + 1)

    return_value = 0
    for i in range(num_batteries):
        return_value += bank[indices[i]] * 10 ** (num_batteries - i - 1)

    return return_value


def part_1(banks: list[list[int]]) -> int:
    return reduce(lambda x, y: x + solve_bank(y, 2), banks, 0)


def part_2(banks: list[list[int]]) -> int:
    return reduce(lambda x, y: x + solve_bank(y, 12), banks, 0)


def main() -> None:
    real_banks = parse_banks(REAL_FILE)
    test_banks = parse_banks(TEST_FILE)

    ans_1 = part_1(test_banks)
    ans_2 = part_2(test_banks)

    print("====== TEST DATA ======")
    print(f"Part 1: {ans_1}       ")
    print(f"Part 2: {ans_2}       ")
    assert ans_1 == 357
    assert ans_2 == 3121910778619

    ans_1 = part_1(real_banks)
    ans_2 = part_2(real_banks)

    print("====== REAL DATA ======")
    print(f"Part 1: {ans_1}       ")
    print(f"Part 2: {ans_2}       ")
    print("=======================")
    assert ans_1 == 17142
    assert ans_2 == 169935154100102


if __name__ == "__main__":
    main()
