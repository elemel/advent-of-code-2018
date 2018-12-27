from collections import defaultdict, deque
from operator import and_, invert, lshift, or_, rshift
from sys import stdin


gates = dict(AND=and_, LSHIFT=lshift, NOT=invert, OR=or_, RSHIFT=rshift)


def parse_part(word):
    if word.isdigit():
        return int(word)
    elif word.islower():
        return word
    elif word.isupper():
        return gates[word]
    else:
        raise ValueError('Invalid part: {word}')


def parse_instruction(line):
    source_str, wire = line.split(' -> ')
    source = [parse_part(s) for s in source_str.split()]
    return source, wire


def provide_signal(source, signals):
    gate = None
    input_signals = []

    for part in source:
        if type(part) == int:
            input_signals.append(part)
        elif type(part) == str:
            if part not in signals:
                return None

            input_signals.append(signals[part])
        else:
            gate = part

    return input_signals[0] if len(source) == 1 else gate(*input_signals)


def main():
    circuit = [parse_instruction(line.strip()) for line in stdin]

    sources = {}
    output_wire_sets = defaultdict(set)

    for source, wire in circuit:
        sources[wire] = source
        input_wires = [token for token in source if type(token) == str]

        for input_wire in input_wires:
            output_wire_sets[input_wire].add(wire)

    signals = {}
    queue = deque(wire for _, wire in circuit)

    while queue:
        wire = queue.popleft()

        if wire in signals:
            continue

        signal = provide_signal(sources[wire], signals)

        if signal is not None:
            signals[wire] = signal
            queue.extend(output_wire_sets[wire])

    print(signals['a'])


if __name__ == '__main__':
    main()
