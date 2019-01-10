from collections import deque
from sys import maxsize, stdin


def knot_hash(s):
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
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

    return ''.join('%02x' % element for element in dense_hash)


def to_bits(h):
    return [int(c) for c in f'{int(h, 16):0128b}']


def main():
    key = stdin.read().strip()

    grid = [
        to_bits(knot_hash(f'{key}-{y}'))
        for y in range(0, 128)
    ]

    stack = [
        (x, y, True)
        for y in range(128)
        for x in range(128)
        if grid[y][x]
    ]

    visited = set()
    region_count = 0

    while stack:
        x, y, seed = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if seed:
            region_count += 1

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= x + dx < 128 and 0 <= y + dy < 128 and grid[y][x]:
                stack.append((x + dx, y + dy, False))

    print(region_count)


if __name__ == '__main__':
    main()
