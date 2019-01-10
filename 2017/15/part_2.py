from sys import stdin


def generate_values(starting_value, factor, multiple):
    value = starting_value

    while True:
        value = (factor * value) % 2147483647

        if value % multiple == 0:
            yield value


def main():
    starting_value_a, starting_value_b = [
        int(line.strip().split()[-1])
        for line in stdin
    ]

    generator_a = generate_values(starting_value_a, 16807, 4)
    generator_b = generate_values(starting_value_b, 48271, 8)

    print(sum(
        next(generator_a) % 65536 == next(generator_b) % 65536
        for _ in range(5_000_000)))


if __name__ == '__main__':
    main()
