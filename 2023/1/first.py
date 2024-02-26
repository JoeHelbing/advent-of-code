import re


def reverse_string(string):
    return string[::-1]


def create_regex(pattern):
    front_pattern = r"^\D*(\d+)"
    back_pattern = r"^\D*(\d+)"
    patterns_list = [pattern for pattern in pattern.keys()]
    for word in patterns_list:
        front_pattern = f"{front_pattern}|^.*({word})"
        back_pattern = f"{back_pattern}|^.*({reverse_string(word)})"

    print(front_pattern)
    print(back_pattern)

    return re.compile(front_pattern), re.compile(back_pattern)


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

    front_pattern, back_pattern = create_regex(word_to_num)
    total = 0
    print(front_pattern)
    print(back_pattern)

    for line in data:
        front = re.search(front_pattern, line)
        back = re.search(back_pattern, line)
        if front:
            # print(front.group(1))
            if front.group(1) in word_to_num:
                total += word_to_num[front.group(1)]
            else:
                total += int(front.group(1))
        if back:
            # print(back.group(1))
            if back.group(1) in word_to_num:
                total += word_to_num[reverse_string(back.group(1))]
            else:
                total += int(back.group(1))
    print("Second Puzzle ", total)
