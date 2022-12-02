"""
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
"""

import os

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

WIN = 6
LOSS = 0
DRAW = 3

shape = {"R": 1, "P": 2, "S": 3}

opponent_map = {"A": "R", "B": "P", "C": "S"}

self_map = {"X": "R", "Y": "P", "Z": "S"}

my_moves = {"X": "lose", "Y": "draw", "Z": "win"}

win_map = {"S": "R", "P": "S", "R": "P"}
loss_map = {"R": "S", "S": "P", "P": "R"}

def main():
    with open(INPUT_TXT) as f:
        score = 0
        for l in f.read().splitlines():
            p1_move, p2_move = l.split(" ")

            if p2_move == "Y":
                score += DRAW
                score += shape[opponent_map[p1_move]]
            elif p2_move == "Z":
                score += WIN
                score += shape[win_map[opponent_map[p1_move]]]
            else:
                score += shape[loss_map[opponent_map[p1_move]]]

    print(f"solution 2: {score}")


if __name__ == "__main__":
    main()


#     score += shape[p2_move]
# KeyError: 'Y'