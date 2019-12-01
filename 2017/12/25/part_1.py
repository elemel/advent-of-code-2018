from collections import defaultdict
from sys import stdin


def parse_transition(lines):
    value_line, new_value_line, move_line, new_state_line = lines
    value = int(value_line[-2])
    new_value = int(new_value_line[-2])
    move = 1 if move_line.endswith(' right.') else -1
    new_state = new_state_line[-2]
    return value, new_value, move, new_state


def parse_state(lines):
    state_line = lines[0]
    state = state_line[-2]
    transitions = parse_transition(lines[1:5]), parse_transition(lines[5:9])
    return state, transitions


def main():
    initial_line, diagnostic_line, _, *state_lines = stdin.read().splitlines()
    state = initial_line[-2]
    step_count = int(diagnostic_line.split()[-2])
    transitions = {}

    for i in range(0, len(state_lines), 10):
        state, value_transitions = parse_state(state_lines[i:(i + 9)])

        for value, new_value, move, new_state in value_transitions:
            transitions[state, value] = new_value, move, new_state

    tape = defaultdict(int)
    cursor = 0

    for _ in range(step_count):
        value = tape[cursor]
        value, move, state = transitions[state, value]
        tape[cursor] = value
        cursor += move

    print(sum(tape.values()))


if __name__ == '__main__':
    main()
