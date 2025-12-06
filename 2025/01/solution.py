from typing import TextIO

DIAL_SIZE = 100
START = 50
FILE = "files/input.txt"


def parse_line(line: str) -> tuple[str, int]:
    direction = line[0]
    number = int(line[1:])
    return direction, number


def part_1(file: TextIO) -> int:
    combination = START
    zeroes = 0
    for line in file:
        direction, number = parse_line(line)

        polarity = -1 if direction == "L" else 1
        combination = (combination + polarity * number) % DIAL_SIZE
        if combination == 0:
            zeroes += 1

    return zeroes


def part_2(file: TextIO) -> int:
    combination = START
    zeroes = 0
    for line in file:
        direction, number = parse_line(line)
        polarity = -1 if direction == "L" else 1
        new_combination = combination + polarity * number

        n = combination + 1 * polarity
        while (direction == "L" and n >= new_combination) or (
            direction == "R" and n <= new_combination
        ):
            if n % DIAL_SIZE == 0:
                zeroes += 1
            n += 1 * polarity

        combination = new_combination % DIAL_SIZE

    return zeroes


def main() -> None:
    with open(FILE, "r", encoding="utf-8") as file:
        print(f"Part 1: {part_1(file)}")
        file.seek(0)
        print(f"Part 2: {part_2(file)}")


if __name__ == "__main__":
    main()
