from collections import Counter
from sys import stdin


def main():
    box_ids = [line.strip() for line in stdin]
    checksum_counts = Counter()

    for id_ in box_ids:
        letter_counts = Counter(id_)
        checksum_counts.update(set(letter_counts.values()))

    print(checksum_counts[2] * checksum_counts[3])


if __name__ == '__main__':
    main()
