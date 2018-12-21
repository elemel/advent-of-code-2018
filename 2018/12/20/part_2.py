from collections import deque
from sys import maxsize, stdin


def get_transitions(regex, i):
    if regex[i] == '^':
        return [(i + 1, 0, 0)]
    elif regex[i] == 'N':
        return [(i + 1, -1, 0)]
    elif regex[i] == 'W':
        return [(i + 1, 0, -1)]
    elif regex[i] == 'E':
        return [(i + 1, 0, 1)]
    elif regex[i] == 'S':
        return [(i + 1, 1, 0)]
    elif regex[i] == '(':
        transitions = [(i + 1, 0, 0)]
        i += 1
        depth = 0

        while regex[i] != ')' or depth != 0:
            if regex[i] == '(':
                depth += 1
            elif regex[i] == '|' and depth == 0:
                transitions.append((i + 1, 0, 0))
            elif regex[i] == ')':
                depth -= 1

            i += 1

        return transitions
    elif regex[i] == '|':
        i += 1
        depth = 0

        while regex[i] != ')' or depth != 0:
            if regex[i] == '(':
                depth += 1
            elif regex[i] == ')':
                depth -= 1

            i += 1

        return [(i + 1, 0, 0)]
    elif regex[i] == ')':
        return [(i + 1, 0, 0)]
    elif regex[i] == '$':
        return []


def print_map(rooms, doors):
    min_y = min(y for y, _ in rooms)
    max_y = max(y for y, _ in rooms)
    min_x = min(x for _, x in rooms)
    max_x = max(x for _, x in rooms)

    grid = [
        [
            '.' if y % 2 == 0 and x % 2 == 0 else '#'
            for x in range(min_x - 1, max_x + 2)
        ]
        for y in range(min_y - 1, max_y + 2)
    ]

    for y, x in doors:
        grid[y - min_y + 1][x - min_x + 1] = '|' if y % 2 == 0 else '-'

    for row in grid:
        print(''.join(row))


def main():
    regex = ''.join(line.strip() for line in stdin)

    transitions = {
        i: get_transitions(regex, i)
        for i in range(len(regex))
    }

    queue = deque([(0, 0, 0, 0)])
    path_distances = {}
    room_distances = {}
    doors = set()

    while queue:
        distance, y, x, i = queue.popleft()

        if distance >= path_distances.get((y, x, i), maxsize):
            continue

        path_distances[y, x, i] = distance

        room_distances[y, x] = min(
            distance, room_distances.get((y, x), maxsize))

        for j, dy, dx in transitions[i]:
            if dy + dx == 0:
                queue.appendleft((distance, y, x, j))
            else:
                doors.add((y + dy, x + dx))
                queue.append((distance + 1, y + 2 * dy, x + 2 * dx, j))

    # print_map(room_distances.keys(), doors)

    print(sum(distance >= 1000 for distance in room_distances.values()))


if __name__ == '__main__':
    main()
