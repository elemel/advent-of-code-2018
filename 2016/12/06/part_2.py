from collections import Counter
from sys import stdin


def main():
    messages = [line.strip() for line in stdin]
    counters = [Counter() for _ in range(8)]

    for message in messages:
        for i, character in enumerate(message):
            counters[i][character] += 1

    print(''.join(counter.most_common()[-1][0] for counter in counters))


if __name__ == '__main__':
    main()
