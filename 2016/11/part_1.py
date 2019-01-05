from collections import deque
from itertools import permutations
from sys import maxsize, stdin


def parse_floor(line):
    items = []

    if ' contains a ' in line:
        _, line = line.split(' contains ')
        line = line[:-1].replace(', and ', ', ').replace(' and ', ', ')

        for part in line.split(', '):
            part = part[2:].replace('-compatible ', ' ')
            material, category = part.split()
            items.append((material, category))

    return tuple(sorted(items))


def is_done(floors):
    return all(not items for floor, items in enumerate(floors) if floor != 3)


def is_safe(items):
    generators = [m for m, c in items if c == 'generator']
    microchips = [m for m, c in items if c == 'microchip']
    return not generators or all(m in generators for m in microchips)


def remove_items(items, floor_items):
    return tuple(item for item in floor_items if item not in items)


def add_items(items, floor_items):
    return tuple(sorted(floor_items + items))


def generate_neighbors(source_floor, floors):
    target_floors = []

    if source_floor > 0:
        target_floors.append(source_floor - 1)

    if source_floor < 3:
        target_floors.append(source_floor + 1)

    source_items = floors[source_floor]
    item_tuples = []

    for i, item in enumerate(source_items):
        item_tuples.append((item,))

        if len(source_items) >= 2:
            for j in range(i + 1, len(source_items)):
                item_tuples.append((item, source_items[j]))

    for items in item_tuples:
        new_source_items = remove_items(items, source_items)

        if not is_safe(new_source_items):
            continue

        for target_floor in target_floors:
            new_target_items = add_items(items, floors[target_floor])

            if not is_safe(new_target_items):
                continue

            new_floors = list(floors)
            new_floors[source_floor] = new_source_items
            new_floors[target_floor] = new_target_items
            yield target_floor, tuple(new_floors)


def main():
    floors = tuple(parse_floor(line.strip()) for line in stdin)
    queue = deque([(0, 0, floors)])
    visited = {}

    while queue:
        step, floor, floors = queue.popleft()

        if is_done(floors):
            print(step)
            return

        if step >= visited.get((floor, floors), maxsize):
            continue

        visited[floor, floors] = step

        for new_floor, new_floors in generate_neighbors(floor, floors):
            queue.append((step + 1, new_floor, new_floors))


if __name__ == '__main__':
    main()
