from collections import defaultdict, deque
from sys import stdin


def parse_instruction(line):
    types = [s for s in line.split() if s in ['value', 'bot', 'output']]
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    numbers = [int(s) for s in number_line.split()]
    return tuple(zip(types, numbers))


def main():
    instructions = deque(parse_instruction(line.strip()) for line in stdin)
    objects = defaultdict(list)

    while instructions:
        instruction = instructions.popleft()

        if len(instruction) == 2:
            (_, number_a), key_b = instruction
            objects[key_b].append(number_a)
        elif len(instruction) == 3:
            key_a, key_b, key_c = instruction

            if len(objects[key_a]) < 2:
                instructions.append(instruction)
                continue

            low, high = sorted(objects[key_a])
            objects[key_b].append(low)
            objects[key_c].append(high)

    value_0, value_1, value_2 = (
        values[0]
        for ((type_, number), values) in objects.items()
        if type_ == 'output' and number <= 2)

    print(value_0 * value_1 * value_2)

if __name__ == '__main__':
    main()
