from sys import maxsize, stdin


weapons_str = """
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""


armor_items_str = """
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""


rings_str = """
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


class Character:
    def __init__(self, name, hit_points, damage, armor):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor


class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


def parse_stats(lines):
    stats = {}

    for line in lines:
        stat_str, value_str = line.split(': ')
        stat = stat_str.lower().replace(' ', '_')
        stats[stat] = int(value_str)

    return stats


def parse_item(line):
    words = line.split()
    name = ''.join(words[:-3])
    cost, damage, armor = [int(s) for s in words[-3:]]
    return Item(name=name, cost=cost, damage=damage, armor=armor)


def attack(attacker, defender):
    damage = max(1, attacker.damage - defender.armor)
    defender.hit_points -= damage

    # print(
    #     f'The {attacker.name} deals {damage} damage; '
    #     f'the {defender.name} goes down to {defender.hit_points} hit points.')


def fight(player, boss):
    while True:
        attack(player, boss)

        if boss.hit_points <= 0:
            return player

        attack(boss, player)

        if player.hit_points <= 0:
            return boss


def main():
    boss_stats = parse_stats(stdin.read().splitlines())
    weapons = [parse_item(line) for line in weapons_str.strip().splitlines()]

    armor_items = [
        parse_item(line)
        for line in armor_items_str.strip().splitlines()
    ]

    rings = [parse_item(line) for line in rings_str.strip().splitlines()]

    max_cost = -1

    for weapon in weapons:
        for armor_item in [None] + armor_items:
            for ring_1 in [None] + rings:
                for ring_2 in [None] + rings:
                    if ring_1 is not None and ring_1 is ring_2:
                        continue

                    items = [
                        item
                        for item in [weapon, armor_item, ring_1, ring_2]
                        if item is not None
                    ]

                    damage = sum(item.damage for item in items)
                    armor = sum(item.armor for item in items)
                    cost = sum(item.cost for item in items)

                    player = Character(
                        name='player',
                        hit_points=100,
                        damage=damage,
                        armor=armor)

                    boss = Character(name='boss', **boss_stats)
                    winner = fight(player, boss)

                    if winner is boss:
                        max_cost = max(max_cost, cost)

    print(max_cost)


if __name__ == '__main__':
    main()
