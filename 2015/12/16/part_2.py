from sys import stdin


message_str = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""


def parse_aunt(line):
    head, tail = line.split(': ', 1)
    number = int(head[4:])
    things = {}

    for part in tail.split(', '):
        key, value_str = part.split(': ')
        things[key] = int(value_str)

    return number, things


def parse_message(message_str):
    message = {}

    for line in message_str.strip().splitlines():
        key, value_str = line.split(': ')
        message[key] = int(value_str)

    return message


def match_thing(key, value, message):
    if key in ['cats', 'trees']:
        return value > message[key]
    elif key in ['pomeranians', 'goldfish']:
        return value < message[key]
    else:
        return value == message[key]
    

def main():
    aunts = dict(parse_aunt(line.strip()) for line in stdin)
    message = parse_message(message_str)

    [number] = [
        number
        for number, things in aunts.items()
        if all(
            match_thing(key, value, message)
            for key, value in things.items())
    ]

    print(number)


if __name__ == '__main__':
    main()
