from collections import Counter
from sys import stdin


def parse_program(line):
    words = line.split()
    name = words[0]
    weight = int(words[1][1:-1])

    if len(words) > 3:
        children = [word.strip(',') for word in words[3:]]
    else:
        children = []

    return name, weight, children


def solve(name, weights, child_lists, total_weights):
    for child in child_lists[name]:
        result = solve(child, weights, child_lists, total_weights)

        if result is not None:
            return result

    counter = Counter(total_weights[child] for child in child_lists[name])

    if len(counter) == 2:
        (common_weight, _), (uncommon_weight, _) = counter.most_common()

        for child in child_lists[name]:
            if total_weights[child] == uncommon_weight:
                return common_weight - (total_weights[child] - weights[child])

    total_weights[name] = weights[name] + sum(counter.elements())
    return None


def main():
    programs = [parse_program(line) for line in stdin]

    weights = {name: weight for name, weight, _ in programs}
    child_lists = {name: children for name, _, children in programs}

    all_children = set(
        child
        for children in child_lists.values()
        for child in children)

    for name, _, _ in programs:
        if name not in all_children:
            print(solve(name, weights, child_lists, {}))


if __name__ == '__main__':
    main()
