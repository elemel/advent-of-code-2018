from sys import maxsize, stdin


def parse_initial_state(line):
    head, tail = line.split(':')
    return tail.strip()


def parse_note(line):
    head, tail = line.split('=>')
    return head.strip(), tail.strip()


def main():
    state = parse_initial_state(stdin.readline())
    stdin.readline()
    notes = dict(parse_note(line) for line in stdin)

    offset = state.find('#')
    state.strip('.')
    generation = 0

    while True:
        old_state = state
        old_offset = offset

        generation += 1
        state = '...' + state + '...'

        state = ''.join(
            notes.get(state[i - 2:i + 3], '.')
            for i in range(len(state)))

        offset += state.find('#') - 3
        state = state.strip('.')

        if state == old_state:
            break

    future_offset = offset + (offset - old_offset) * (50000000000 - generation)
    print(sum(i + future_offset for i, pot in enumerate(state) if pot == '#'))


if __name__ == '__main__':
    main()
