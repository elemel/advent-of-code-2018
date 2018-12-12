from sys import stdin


def parse_initial_state(line):
    head, tail = line.split(':')
    return tail.strip()


def parse_note(line):
    head, tail = line.split('=>')
    return head.strip(), tail.strip()


def main():
    initial_state = parse_initial_state(stdin.readline())
    stdin.readline()
    notes = dict(parse_note(line) for line in stdin)
    padding = 2 * 20

    state = padding * '.' + initial_state + padding * '.'

    for i in range(20):
        state = ''.join(
            notes.get(state[i - 2:i + 3], '.') for i in range(len(state)))

    print(sum(i - padding for i, pot in enumerate(state) if pot == '#'))


if __name__ == '__main__':
    main()
