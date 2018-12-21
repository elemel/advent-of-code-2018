from itertools import combinations
from sys import stdin


def main():
    box_ids = [line.strip() for line in stdin]

    for id_1, id_2 in combinations(box_ids, 2):
        if len(id_1) == len(id_2):
            common_letters = ''.join(
                letter_1
                for letter_1, letter_2 in zip(id_1, id_2)
                if letter_1 == letter_2)

            if len(common_letters) == len(id_1) - 1:
                print(common_letters)
                return


if __name__ == '__main__':
    main()
