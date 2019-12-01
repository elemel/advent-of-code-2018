from sys import stdin


def solve(compressed_data):
    repeated_data = []
    decompressed_length = 0

    while compressed_data:
        char = compressed_data.pop()

        if char != '(':
            decompressed_length += 1
            continue

        while True:
            char = compressed_data.pop()

            if char == ')':
                break

            repeated_data.append(char)

        n, x = [int(s) for s in ''.join(repeated_data).split('x')]
        repeated_data.clear()

        for _ in range(n):
            repeated_data.append(compressed_data.pop())

        repeated_data.reverse()
        decompressed_length += x * solve(repeated_data)

    return decompressed_length


def main():
    compressed_data = []

    for line in stdin:
        compressed_data.extend(line.strip())

    compressed_data.reverse()
    print(solve(compressed_data))


if __name__ == '__main__':
    main()
