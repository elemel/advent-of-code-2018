from sys import stdin


def solve(node):
    child_count = node.pop()
    metadata_count = node.pop()

    if not child_count:
        return sum(node.pop() for _ in range(metadata_count))

    child_values = [solve(node) for _ in range(child_count)]
    metadata_entries = [node.pop() for _ in range(metadata_count)]

    return sum(
        child_values[i - 1]
        for i in metadata_entries
        if 1 <= i <= len(child_values))


def main():
    node = [int(s) for s in stdin.read().split()]
    node.reverse()
    print(solve(node))


if __name__ == '__main__':
    main()
