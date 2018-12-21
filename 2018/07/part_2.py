from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin


def parse_requirement(line):
    words = line.split()
    return words[1], words[-3]


def get_duration(step):
    return 60 + ord(step) - ord('A') + 1


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

    second = 0
    in_progress = []
    completed = []

    while available or in_progress:
        while available and len(in_progress) < 5:
            parent = heappop(available)
            heappush(in_progress, (second + get_duration(parent), parent))

        second, parent = heappop(in_progress)

        for child in children[parent]:
            parents[child].remove(parent)

            if not parents[child]:
                heappush(available, child)

        completed.append(parent)

    print(second)


if __name__ == '__main__':
    main()
