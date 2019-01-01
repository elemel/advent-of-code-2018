from collections import namedtuple
from heapq import heappop, heappush
from sys import maxsize, stdin


StateTuple = namedtuple('State', """
    turn
    player_hit_points
    player_mana_points
    player_armor
    boss_hit_points
    boss_damage
    shield_timer
    poison_timer
    recharge_timer
""")


class State:
    __slots__ = StateTuple._fields

    def __init__(self, *args, **kwargs):
        for k, v in zip(StateTuple._fields, args):
            setattr(self, k, v)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        for k in StateTuple._fields:
            yield getattr(self, k)


def log(message=''):
    pass # print(message)


def main():
    boss_hit_points, boss_damage = [int(line.split()[-1]) for line in stdin]

    state_tuple = StateTuple(
        turn='player',
        player_hit_points=50,
        player_mana_points=500,
        player_armor=0,
        boss_hit_points=boss_hit_points,
        boss_damage=boss_damage,
        shield_timer=0,
        poison_timer=0,
        recharge_timer=0)

    queue = [(0, state_tuple)]
    seen = {}

    while queue:
        spent_mana_points, state_tuple = heappop(queue)

        if seen.get(state_tuple, maxsize) <= spent_mana_points:
            continue

        seen[state_tuple] = spent_mana_points
        state = State(*state_tuple)

        log()
        log(f'-- {state.turn.capitalize()} turn --')

        log(
            f'- Player has {state.player_hit_points} hit points, '
            f'{state.player_armor} armor, '
            f'{state.player_mana_points} mana')

        log(f'- Boss has {state.boss_hit_points} hit points')

        if state.turn == 'player':
            state.player_hit_points -= 1

        if state.shield_timer:
            state.shield_timer -= 1

            if not state.shield_timer:
                state.player_armor -= 7

        if state.poison_timer:
            state.poison_timer -= 1
            state.boss_hit_points -= 3

        if state.recharge_timer:
            state.recharge_timer -= 1
            state.player_mana_points += 101

        if state.player_hit_points <= 0:
            continue

        if state.boss_hit_points <= 0:
            print(spent_mana_points)
            return

        if state.turn == 'player':
            if state.player_mana_points >= 53:
                state_2 = State(*state, turn='boss')
                state_2.player_mana_points -= 53
                state_2.boss_hit_points -= 4
                log('Player casts Magic Missile, dealing 4 damage.')
                heappush(queue, (spent_mana_points + 53, StateTuple(*state_2)))

            if state.player_mana_points >= 73:
                state_2 = State(*state, turn='boss')
                state_2.player_mana_points -= 73
                state_2.player_hit_points += 2
                state_2.boss_hit_points -= 2

                log(
                    'Player casts Drain, '
                    'dealing 2 damage, '
                    'and healing 2 hit points.')

                heappush(queue, (spent_mana_points + 73, StateTuple(*state_2)))

            if state.player_mana_points >= 113 and not state.shield_timer:
                state_2 = State(*state, turn='boss')
                state_2.player_mana_points -= 113
                state_2.player_armor += 7
                state_2.shield_timer = 6
                log('Player casts Shield, increasing armor by 7.')
                heappush(queue, (spent_mana_points + 113, StateTuple(*state_2)))

            if state.player_mana_points >= 173 and not state.poison_timer:
                state_2 = State(*state, turn='boss')
                state_2.player_mana_points -= 173
                state_2.poison_timer = 6
                log('Player casts Poison.')
                heappush(queue, (spent_mana_points + 173, StateTuple(*state_2)))

            if state.player_mana_points >= 229 and not state.recharge_timer:
                state_2 = State(*state, turn='boss')
                state_2.player_mana_points -= 229
                state_2.recharge_timer = 5
                log('Player casts Recharge.')
                heappush(queue, (spent_mana_points + 229, StateTuple(*state_2)))
        else:
            state_2 = State(*state, turn='player')
            damage = max(1, state_2.boss_damage - state_2.player_armor)
            state_2.player_hit_points -= damage
            log(f'Boss attacks for {damage} damage!')
            heappush(queue, (spent_mana_points, StateTuple(*state_2)))


if __name__ == '__main__':
    main()
