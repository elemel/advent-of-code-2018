from sys import maxsize, stdin


class Group:
    def __init__(
        self,
        army,
        number,
        units,
        hit_points,
        weaknesses,
        immunities,
        attack_damage,
        attack_type,
        initiative):

        self.army = army
        self.number = number
        self.units = units
        self.hit_points = hit_points
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative

    def __repr__(self):
        return f'Group(army={self.army}, number={self.number})'


def get_effective_power(attacker):
    return attacker.units * attacker.attack_damage


def get_effective_damage(attacker, target):
    if attacker.attack_type in target.immunities:
        return 0
    elif attacker.attack_type in target.weaknesses:
        return 2 * get_effective_power(attacker)
    else:
        return get_effective_power(attacker)


def parse_group(line, army, number, boost):
    words = line.split()

    units = int(words[0])
    hit_points = int(words[4])
    weaknesses = set()
    immunities = set()

    middle_words = words[7:-11]

    if middle_words:
        middle_str = ' '.join(middle_words).strip('()')

        for part in middle_str.split('; '):
            if part.startswith('weak to '):
                weaknesses = part[8:].split(', ')
            elif part.startswith('immune to '):
                immunities = part[10:].split(', ')

    attack_damage = int(words[-6]) + boost
    attack_type = words[-5]
    initiative = int(words[-1])

    return Group(
        army=army,
        number=number,
        units=units,
        hit_points=hit_points,
        weaknesses=weaknesses,
        immunities=immunities,
        attack_damage=attack_damage,
        attack_type=attack_type,
        initiative=initiative)


def main():
    lines = [line.strip() for line in stdin]
    i = lines.index('')

    for boost in range(0, maxsize):
        immune_system = [
            parse_group(line, 'immune_system', j + 1, boost)
            for j, line in enumerate(lines[1:i])
        ]

        infection = [
            parse_group(line, 'infection', j + 1, 0)
            for j, line in enumerate(lines[i + 2:])
        ]

        while immune_system and infection:
            groups = immune_system + infection
            attackers_to_targets = {}
            targets_to_attackers = {}

            def target_selection_key(attacker):
                return -get_effective_power(attacker), -attacker.initiative

            groups.sort(key=target_selection_key)

            for attacker in groups:
                available_targets = [
                    target for target in groups
                    if target not in targets_to_attackers
                    and target.army != attacker.army
                    and get_effective_damage(attacker, target) > 0]

                if available_targets:
                    def targeting_key(target):
                        return (
                            get_effective_damage(attacker, target),
                            get_effective_power(target),
                            target.initiative)

                    selected_target = max(available_targets, key=targeting_key)
                    attackers_to_targets[attacker] = selected_target
                    targets_to_attackers[selected_target] = attacker

            attackers = list(attackers_to_targets)

            if not attackers:
                break

            def attacking_key(attacker):
                return -attacker.initiative

            attackers.sort(key=attacking_key)

            for attacker in attackers:
                target = attackers_to_targets[attacker]

                effective_damage = get_effective_damage(attacker, target)

                killed_units = min(
                    target.units,
                    effective_damage // target.hit_points)

                target.units -= killed_units

            immune_system = [
                group for group in immune_system if group.units > 0
            ]

            infection = [group for group in infection if group.units > 0]

        if immune_system and not infection:
            break

    print(sum(group.units for group in immune_system + infection))


if __name__ == '__main__':
    main()
