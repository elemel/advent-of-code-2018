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


def decrypt_letter(letter, sector_id):
    return chr((ord(letter) - ord('a') + sector_id) % 26 + ord('a'))


def decrypt_room_name(encrypted_name, sector_id):
    return ''.join(
        ' ' if c == '-' else decrypt_letter(c, sector_id)
        for c in encrypted_name)


def main():
    rooms = [parse_room(line.strip()) for line in stdin]

    for encrypted_name, sector_id, checksum in rooms:
        if is_real_room(encrypted_name, checksum):
            decrypted_name = decrypt_room_name(encrypted_name, sector_id)

            if decrypted_name == 'northpole object storage':
                print(sector_id)
                return


if __name__ == '__main__':
    main()
