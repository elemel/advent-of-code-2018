from collections import deque, OrderedDict
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

    return items


def is_done(floors):
    return not any(floors[:-1])


def is_safe(items):
    generators = [m for m, c in items if c == 'generator']
    microchips = [m for m, c in items if c == 'microchip']
    return not generators or all(m in generators for m in microchips)


def generate_neighbors(source_floor, floors):
    target_floors = [
        i
        for i in [source_floor - 1, source_floor + 1]
        if 0 <= i < len(floors)
    ]

    source_items = floors[source_floor]
    item_lists = []

    for i, item in enumerate(source_items):
        item_lists.append([item])

        if len(source_items) >= 2:
            for j in range(i + 1, len(source_items)):
                item_lists.append([item, source_items[j]])

    for items in item_lists:
        new_source_items = [item for item in source_items if item not in items]

        if not is_safe(new_source_items):
            continue

        for target_floor in target_floors:
            new_target_items = floors[target_floor] + items

            if not is_safe(new_target_items):
                continue

            new_floors = list(floors)
            new_floors[source_floor] = new_source_items
            new_floors[target_floor] = new_target_items
            yield target_floor, new_floors


def to_key(floor, floors, materials, categories):
    for i, items in enumerate(floors):
        for material, category in items:
            j = materials[material]
            categories[category][j] = i

    return floor, tuple(sorted(zip(*categories.values())))


def main():
    floors = [parse_floor(line.strip()) for line in stdin]

    extra_items = [
        (material, category)
        for material in ('dilithium', 'elerium')
        for category in ('generator', 'microchip')
    ]

    floors[0] += extra_items

    materials = {}
    generators = []
    microchips = []
    categories = OrderedDict(generator=generators, microchip=microchips)

    for i, items in enumerate(floors):
        for material, category in items:
            if material not in materials:
                materials[material] = len(materials)
                generators.append(-1)
                microchips.append(-1)

    queue = deque([[0, 0, floors]])
    visited = set()

    while queue:
        step, floor, floors = queue.popleft()
        key = to_key(floor, floors, materials, categories)

        if key in visited:
            continue

        visited.add(key)

        if is_done(floors):
            print(step)
            return

        for new_floor, new_floors in generate_neighbors(floor, floors):
            queue.append([step + 1, new_floor, new_floors])


if __name__ == '__main__':
    main()
