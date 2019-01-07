from collections import deque
from sys import maxsize, stdin


def parse_node(line):
    digit_line = ''.join(c if c.isdigit() else ' ' for c in line)
    x, y, _, used, avail, _ = [int(s) for s in digit_line.split()]
    return (x, y), (used, avail)


def main():
    _, _, *node_lines = stdin.read().splitlines()
    nodes = dict(parse_node(line) for line in node_lines)

    [(hole_x, hole_y)] = [
        (x, y)
        for (x, y), (used, avail) in nodes.items()
        if used == 0
    ]

    goal_x, goal_y = max(x for x, y in nodes), 0
    queue = deque([(0, hole_x, hole_y, goal_x, goal_y)])
    visited = set()

    while queue:
        step, hole_x, hole_y, goal_x, goal_y = queue.popleft()

        if (hole_x, hole_y, goal_x, goal_y) in visited:
            continue

        visited.add((hole_x, hole_y, goal_x, goal_y))

        if (goal_x, goal_y) == (0, 0):
            print(step)
            return

        hole_used, hole_avail = nodes[hole_x, hole_y]

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_hole_x, new_hole_y = hole_x + dx, hole_y + dy

            if (new_hole_x, new_hole_y) not in nodes:
                continue

            new_hole_used, _ = nodes[new_hole_x, new_hole_y]

            if new_hole_used > hole_used + hole_avail:
                continue

            new_goal_x, new_goal_y = goal_x, goal_y

            if (new_hole_x, new_hole_y) == (goal_x, goal_y):
                new_goal_x, new_goal_y = hole_x, hole_y

            queue.append(
                (step + 1, new_hole_x, new_hole_y, new_goal_x, new_goal_y))


if __name__ == '__main__':
    main()
