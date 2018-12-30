from sys import stdin


def solve(eggnog, containers):
    if eggnog == 0:
        return 1

    if not containers:
        return 0

    size = containers.pop()
    combinations = solve(eggnog, containers)

    if size <= eggnog:
        eggnog -= size
        combinations += solve(eggnog, containers)

    containers.append(size)
    return combinations


def main():
    containers = [int(line.strip()) for line in stdin]
    print(solve(150, containers))


if __name__ == '__main__':
    main()
