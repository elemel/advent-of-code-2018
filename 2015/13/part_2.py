from collections import defaultdict
from itertools import permutations
from sys import stdin


def parse_change(line):
    words = line[:-1].split()
    change = -int(words[3]) if words[2] == 'lose' else int(words[3])
    return words[0], change, words[-1]


def get_total_change(seating_arrangement, change_dicts):
    total_change = 0

    for i, guest in enumerate(seating_arrangement):
        neighbor_1 = seating_arrangement[(i - 1) % len(seating_arrangement)]
        neighbor_2 = seating_arrangement[(i + 1) % len(seating_arrangement)]

        total_change += (
            change_dicts[guest][neighbor_1] +
            change_dicts[guest][neighbor_2])

    return total_change


def main():
    changes = [parse_change(line.strip()) for line in stdin]
    change_dicts = defaultdict(dict)

    for guest_1, change, guest_2, in changes:
        change_dicts[guest_1][guest_2] = change

    guests = list(change_dicts.keys())

    for guest in guests:
        change_dicts['you'][guest] = 0
        change_dicts[guest]['you'] = 0

    guests.append('you')
    guests.sort()

    max_total_change = max(
        get_total_change(seating_arrangement, change_dicts)
        for seating_arrangement in permutations(guests))

    print(max_total_change)


if __name__ == '__main__':
    main()
