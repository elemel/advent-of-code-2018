from collections import defaultdict
from sys import stdin


def parse_room(line):
    i = line.rfind('-')
    encrypted_name = line[:i]
    sector_id_str, checksum = line[i:][1:-1].split('[')
    return encrypted_name, int(sector_id_str), checksum


def is_real_room(encrypted_name, checksum):
    letter_counts = defaultdict(int)

    for letter in encrypted_name.replace('-', ''):
        letter_counts[letter] += 1

    most_common = sorted(
        (-count, letter)
        for letter, count in letter_counts.items())

    return checksum == ''.join(letter for _, letter in most_common[:5])


def main():
    rooms = [parse_room(line.strip()) for line in stdin]

    print(sum(
        sector_id
        for encrypted_name, sector_id, checksum in rooms
        if is_real_room(encrypted_name, checksum)))


if __name__ == '__main__':
    main()
