import re
import os


EMPTY_LINE_REGEX = r"(?:\r?\n){2,}"
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def main():

    with open(INPUT_TXT) as f:
        results = []
        elves = re.split(EMPTY_LINE_REGEX, f.read().strip())
        for elf in elves:
            results.append(sum([int(i) for i in elf.split('\n')]))
    
    print(f"solution 1: {max(results)}")
    print(f"solution 2: {sum(sorted(results)[-3:])}")


if __name__ == "__main__":
    main()

