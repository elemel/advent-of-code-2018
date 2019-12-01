from sys import stdin


def parse_program(line):
    head, tail = line.split('<->')
    id = int(head)
    connections = [int(s) for s in tail.split(',')]
    return id, connections


def main():
    programs = dict(parse_program(line) for line in stdin)
    groups = {}
    stack = []
    group_count = 0

    for id in programs:
        if id not in groups:
            group_count += 1
            group = set()
            stack.append(id)

            while stack:
                connection = stack.pop()

                if connection not in group:
                    group.add(connection)
                    groups[connection] = group
                    stack.extend(programs[connection])

    print(group_count)


if __name__ == '__main__':
    main()
