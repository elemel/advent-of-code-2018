from sys import stdin


def main():
    lengths = [ord(c) for c in stdin.read().strip()]
    lengths.extend([17, 31, 73, 47, 23])
    numbers = list(range(256))
    position = 0
    skip_size = 0

    for round in range(64):
        for length in lengths:
            for i in range(0, length // 2):
                j = (position + i) % len(numbers)
                k = (position + length - 1 - i) % len(numbers)
                numbers[j], numbers[k] = numbers[k], numbers[j]

            position = (position + length + skip_size) % len(numbers)
            skip_size += 1

    dense_hash = 16 * [0]

    for i, number in enumerate(numbers):
        dense_hash[i // 16] ^= number

    print(''.join('%02x' % element for element in dense_hash))


if __name__ == '__main__':
    main()
