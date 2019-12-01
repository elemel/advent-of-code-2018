from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin


def parse_requirement(line):
    words = line.split()
    return words[1], words[-3]


def main():
    requirements = [parse_requirement(line) for line in stdin]

    children = defaultdict(set)
    parents = defaultdict(set)

    for parent, child in requirements:
        children[parent].add(child)
        parents[child].add(parent)

    available = []

    for parent in children:
        if not parents[parent]:
            heappush(available, parent)

    completed = []

    while available:
        parent = heappop(available)

        for child in children[parent]:
            parents[child].remove(parent)

            if not parents[child]:
                heappush(available, child)

        completed.append(parent)

    print(''.join(completed))


if __name__ == '__main__':
    main()
