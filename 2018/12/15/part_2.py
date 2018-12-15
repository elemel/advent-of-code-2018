from collections import defaultdict, deque
from sys import maxsize, stdin


directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]


class Unit:
    def __init__(self, type, x, y, hit_points):
        self.type = type
        self.x = x
        self.y = y
        self.hit_points = hit_points

    def __str__(self):
        return self.type


def find_path(map, unit):
    target_str = 'E' if str(unit) == 'G' else 'G'

    open = deque([(unit.x, unit.y)])
    closed = set([(unit.x, unit.y)])
    parents = {}

    while open:
        x, y = open.popleft()

        for dx, dy in directions:
            if (x + dx, y + dy) in closed:
                continue

            square = map[y + dy][x + dx]

            if str(square) == target_str:
                path = []

                while (x, y) != (unit.x, unit.y):
                    path.append((x, y))
                    x, y = parents[x, y]

                return path

            if square == '.':
                parents[x + dx, y + dy] = x, y
                open.append((x + dx, y + dy))

            closed.add((x + dx, y + dy))

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
        unit_counts = dict(E=0, G=0)

        for y, row in enumerate(map):
            for x, square in enumerate(row):
                if square in 'EG':
                    unit = Unit(
                        type=square,
                        x=x,
                        y=y,
                        hit_points=200)

                    map[y][x] = unit
                    units.append(unit)
                    unit_counts[square] += 1

        original_elf_count = unit_counts['E']

        round = 0
        turn = 0

        while unit_counts['E'] == original_elf_count and unit_counts['G'] > 0:
            unit = units[turn]

            if unit.hit_points > 0:
                path = find_path(map, unit)

                if path:
                    map[unit.y][unit.x] = '.'
                    unit.x, unit.y = path[-1]
                    map[unit.y][unit.x] = unit

                target = find_target(map, unit)

                if target:
                    attack_power = elf_attack_power if str(unit) == 'E' else 3
                    target.hit_points -= attack_power

                    if target.hit_points <= 0:
                        map[target.y][target.x] = '.'
                        unit_counts[str(target)] -= 1

            turn += 1

            if turn >= len(units):
                round += 1
                units = [unit for unit in units if unit.hit_points > 0]

                def key(a):
                    return a.y, a.x

                units.sort(key=key)
                turn = 0

        if unit_counts['E'] == original_elf_count:
            total_hit_points = sum(max(0, unit.hit_points) for unit in units)
            print(round * total_hit_points)
            return


if __name__ == '__main__':
    main()
