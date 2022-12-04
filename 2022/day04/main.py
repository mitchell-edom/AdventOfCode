import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def main():
    with open(INPUT_TXT) as f:
        first_solution, second_solution = 0, 0
        for line in [x.strip() for x in f.readlines()]:
            a, b = line.split(",")
            a, b = a.split("-"), b.split("-")

            a = set([x for x in range(int(a[0]), int(a[1]) + 1)])  
            b = set([x for x in range(int(b[0]), int(b[1]) + 1)])

            first_solution += int(a.issubset(b) or b.issubset(a))
            second_solution += int(any(a.intersection(b)))

        print(f"solution 1: {first_solution}")
        print(f"solution 2: {second_solution}")

if __name__ == "__main__":
    main()
