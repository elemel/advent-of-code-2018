from collections import defaultdict, deque
from sys import maxsize, stdin


directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


class Unit:
    def __init__(self, type, x, y, attack_power, hit_points):
        self.type = type
        self.x = x
        self.y = y
        self.attack_power = attack_power
        self.hit_points = hit_points

    def __str__(self):
        return self.type

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)


def find_target(map, unit):
    target_type = 'E' if unit.type == 'G' else 'G'
    targets = []

    for dy, dx in directions:
        square = map[unit.y + dy][unit.x + dx]

        if str(square) == target_type:
            targets.append((square.hit_points, square))

    if not targets:
        return None

    _, target = min(targets)
    return target


def move(map, units, unit):
    seen = set()

    queue = deque(sorted(
        (target.y, target.x)
        for target in units
        if target.type != unit.type and target.hit_points != 0))

    while queue:
        y, x = queue.popleft()

        if (y, x) in seen:
            continue

        seen.add((y, x))

        for dy, dx in directions:
            if y + dy == unit.y and x + dx == unit.x:
                map[unit.y][unit.x] = '.'
                unit.y = y
                unit.x = x
                map[unit.y][unit.x] = unit
                return

            if map[y + dy][x + dx] == '.':
                queue.append((y + dy, x + dx))


def attack(map, unit, target, total_hit_points):
    damage = min(unit.attack_power, target.hit_points)
    target.hit_points -= damage
    total_hit_points[target.type] -= damage

    if target.hit_points == 0:
        map[target.y][target.x] = '.'


def main():
    original_map = [list(line.rstrip('\r\n')) for line in stdin]

    for elf_attack_power in range(0, maxsize):
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

        elf_count = sum(unit.type == 'E' for unit in units)
        round = 0
        turn = 0

        while min(total_hit_points.values()) != 0:
            unit = units[turn]

            if unit.hit_points != 0:
                target = find_target(map, unit)

                if not target:
                    move(map, units, unit)
                    target = find_target(map, unit)

                if target:
                    attack(map, unit, target, total_hit_points)

            turn += 1

            if turn >= len(units):
                round += 1
                units = sorted(unit for unit in units if unit.hit_points != 0)
                turn = 0

        if sum(unit.type == 'E' for unit in units) == elf_count:
            print(round * max(total_hit_points.values()))
            return


if __name__ == '__main__':
    main()
