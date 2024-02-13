import re

if __name__ == "__main__":
    with open("2023/1/puzzle_input.txt") as f:
        data = f.read().split("\n")

    # first puzzle
    pattern_front = re.compile(r"^\D*(\d)")
    pattern_back = re.compile(r"(\d)\D*$")

    total = 0
    for line in data:
        front = pattern_front.search(line).group(1)
        back = pattern_back.search(line).group(1)
        full = int(front + back)
        total += full
    print("First Puzzle ", total)

    # second puzzle
    word_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # regex patterns
    front_pattern = re.compile(
        r"^\D*(\d)|\D*(one)|\D*(two)|(three)|\D*(four)|\D*(five)|\D*(six)|\D*(seven)|\D*(eight)|\D*(nine)"
    )
    back_pattern = re.compile(
        r"(\d)\D*$|one\D*$|two\D*$|three\D*$|four\D*$|five\D*$|six\D*$|seven\D*$|eight\D*$|nine\D*$"
    )

    total = 0
    for line in data:
        front = front_pattern.search(line).group(1)
        back = back_pattern.search(line).group(1)
        print(front, back)
        if front is type(str):
            front = word_to_num[front]
        if back is type(str):
            back = word_to_num[back]
        full = int(front + back)
        total += full
    print("Second Puzzle ", total)
