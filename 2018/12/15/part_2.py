from collections import defaultdict, deque
from sys import maxsize, stdin


directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]


class Unit:
    def __init__(self, type, x, y, attack_power, hit_points):
        self.type = type
        self.x = x
        self.y = y
        self.attack_power = attack_power
        self.hit_points = hit_points

    def __str__(self):
        return self.type


def find_path(map, unit):
    target_str = 'E' if str(unit) == 'G' else 'G'

    open = deque([(unit.x, unit.y)])
    closed = set([(unit.x, unit.y)])
    parents = {}

    while open:
        x1, y1 = open.popleft()

        for dx, dy in directions:
            x2 = x1 + dx
            y2 = y1 + dy

            if (x2, y2) in closed:
                continue

            square = map[y2][x2]

            if str(square) == target_str:
                path = []

                while (x1, y1) != (unit.x, unit.y):
                    path.append((x1, y1))
                    x1, y1 = parents[x1, y1]

                return path

            if square == '.':
                parents[x2, y2] = x1, y1
                open.append((x2, y2))

            closed.add((x2, y2))

    return []


def find_target(map, unit):
    target_str = 'E' if str(unit) == 'G' else 'G'
    targets = []

    for dx, dy in directions:
        square = map[unit.y + dy][unit.x + dx]

        if str(square) == target_str:
            targets.append(square)

    if not targets:
        return None

    def key(target):
        return target.hit_points, target.y, target.x

    return min(targets, key=key)


def main():
    original_map = [list(line.rstrip('\r\n')) for line in stdin]

    for elf_attack_power in range(3, maxsize):
        map = [list(row) for row in original_map]

        units = []
        total_hit_points = dict(E=0, G=0)

        for y, row in enumerate(map):
            for x, square in enumerate(row):
                if square in 'EG':
                    attack_power = elf_attack_power if square == 'E' else 3

                    unit = Unit(
                        type=square,
                        x=x,
                        y=y,
                        attack_power=attack_power,
                        hit_points=200)

                    map[y][x] = unit
                    units.append(unit)
                    total_hit_points[square] += unit.hit_points

        elf_count = sum(str(unit) == 'E' for unit in units)
        round = 0
        turn = 0

        while min(total_hit_points.values()) != 0:
            unit = units[turn]

            if unit.hit_points != 0:
                path = find_path(map, unit)

                if path:
                    map[unit.y][unit.x] = '.'
                    unit.x, unit.y = path[-1]
                    map[unit.y][unit.x] = unit

                target = find_target(map, unit)

                if target:
                    damage = min(unit.attack_power, target.hit_points)
                    target.hit_points -= damage
                    total_hit_points[target.type] -= damage

                    if target.hit_points == 0:
                        map[target.y][target.x] = '.'

            turn += 1

            if turn >= len(units):
                round += 1
                units = [unit for unit in units if unit.hit_points > 0]

                def key(a):
                    return a.y, a.x

                units.sort(key=key)
                turn = 0

        if sum(str(unit) == 'E' for unit in units if unit.hit_points > 0) == elf_count:
            print(round * max(total_hit_points.values()))
            return


if __name__ == '__main__':
    main()
