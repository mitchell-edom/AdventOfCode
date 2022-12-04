import os
import string
from typing import Iterable, Union

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

priority_map = {character: score + 1 for (score, character) in enumerate(string.ascii_lowercase)}
priority_map.update({character: score + 27 for (score, character) in enumerate(string.ascii_uppercase)})


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]



def get_intersection(a, b, c):
    set_a = set(a)
    set_b = set(b)
    set_c = set(c)
    r1 = set_a.intersection(set_b)
    result = r1.intersection(set_c)
    return list(result)


def main():
    with open(INPUT_TXT) as f:
        priorities_sum = 0
        for l in f.readlines():
            line = l.strip("\n")
            middle_idx = int(len(line) / 2)
            first_compartment = line[:middle_idx]
            second_compartment = line[middle_idx:]
            duplicate = [x for x in first_compartment if x in second_compartment][0]
            priorities_sum += priority_map[duplicate]
        
    with open(INPUT_TXT) as f:
        all_work = [line.rstrip() for line in f.read().split("\n")]
        badge_sum = 0
        for group in chunks(all_work, 3):
            expected_badge = get_intersection(group[0], group[1], group[2])
            badge_sum += priority_map[expected_badge[0]]


    print(f"solution 1: {priorities_sum}")
    print(f"solution 2: {badge_sum}")

if __name__ == "__main__":
    main()
