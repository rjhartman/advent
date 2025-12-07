from pathlib import Path
from typing import List, Tuple, Literal, Iterable
from functools import reduce

REAL_FILE = Path("files/input.txt")
TEST_FILE = Path("files/test.txt")

Operator = Literal["*", "+"]
ParseResult = Iterable[Tuple[Operator, List[int]]]


def human_parse(file: Path) -> ParseResult:
    lines = file.read_text().strip().splitlines()

    operators = lines[-1].strip().split()
    columns = list([] for _ in range(len(operators)))

    for line in lines[:-1]:
        data = line.strip().split()
        for column, n in zip(columns, data):
            column.append(int(n))

    return zip(operators, columns)


def cephalopod_parse(file: Path) -> ParseResult:
    lines = file.read_text().strip("\n").splitlines()
    y_max = len(lines) - 1

    current = None
    result = []
    for i in range(len(lines[0])):
        number = ""
        if operator := lines[y_max][i].strip():
            if current:
                result.append(tuple(current))
            current = [operator, []]

        for j in range(y_max):
            digit = lines[j][i]
            if digit != " ":
                number += digit

        if number:
            current[1].append(int(number))

    result.append(current)
    return result


def solve(data: ParseResult) -> int:
    total = 0
    for operator, column in data:
        total += reduce(lambda x, y: eval(f"{x}{operator}{y}"), column[1:], column[0])
    return total


def part_1(file: Path) -> int:
    return solve(human_parse(file))


def part_2(file: Path) -> int:
    return solve(cephalopod_parse(file))


def main() -> None:
    ans_1 = part_1(TEST_FILE)
    ans_2 = part_2(TEST_FILE)
    print("====== TEST DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 4277556
    assert ans_2 == 3263827

    ans_1 = part_1(REAL_FILE)
    ans_2 = part_2(REAL_FILE)
    print("====== REAL DATA =======")
    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")
    assert ans_1 == 4693159084994
    assert ans_2 == 11643736116335


if __name__ == "__main__":
    main()
