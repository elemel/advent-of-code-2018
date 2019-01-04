from sys import stdin


def main():
    compressed_data = []

    for line in stdin:
        compressed_data.extend(line.strip())

    compressed_data.reverse()
    repeated_data = []
    decompressed_data = []

    while compressed_data:
        char = compressed_data.pop()

        if char != '(':
            decompressed_data.append(char)
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

        for _ in range(x):
            decompressed_data.extend(repeated_data)

        repeated_data.clear()

    print(len(decompressed_data))


if __name__ == '__main__':
    main()
