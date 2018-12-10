from sys import stdin


def main():
    lengths = [int(s) for s in stdin.read().strip().split(',')]
    numbers = list(range(256))
    position = 0
    skip_size = 0

    for length in lengths:
        for i in range(0, length // 2):
            j = (position + i) % len(numbers)
            k = (position + length - 1 - i) % len(numbers)
            numbers[j], numbers[k] = numbers[k], numbers[j]

        position = (position + length + skip_size) % len(numbers)
        skip_size += 1

    print(numbers[0] * numbers[1])


if __name__ == '__main__':
    main()
