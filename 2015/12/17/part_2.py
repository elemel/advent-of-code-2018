from sys import maxsize, stdin


def solve(eggnog, containers, count):
    if eggnog == 0:
        return 1, count

    if not containers:
        return 0, maxsize

    size = containers.pop()
    combinations, min_count = solve(eggnog, containers, count)

    if size <= eggnog:
        eggnog -= size
        combinations_2, min_count_2 = solve(eggnog, containers, count + 1)

        if min_count_2 < min_count:
            combinations = combinations_2
            min_count = min_count_2
        elif min_count_2 == min_count:
            combinations += combinations_2

    containers.append(size)
    return combinations, min_count


def main():
    containers = [int(line.strip()) for line in stdin]
    combinations, _ = solve(150, containers, 0)
    print(combinations)


if __name__ == '__main__':
    main()
