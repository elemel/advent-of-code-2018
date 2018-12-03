from collections import namedtuple
from sys import stdin


Claim = namedtuple('Claim', ['id', 'x', 'y', 'width', 'height'])


def parse_claim(line):
    id_str, _, position_str, size_str = line.split()
    id = int(id_str[1:])
    x, y = (int(i) for i in position_str[:-1].split(','))
    width, height = (int(i) for i in size_str.split('x'))
    return Claim(id=id, x=x, y=y, width=width, height=height)


def add_claim_to_fabric(claim, fabric):
    for x in range(claim.x, claim.x + claim.width):
        for y in range(claim.y, claim.y + claim.height):
            fabric[y][x].add(claim.id)


def main():
    claims = [parse_claim(line) for line in stdin]
    fabric_width = max(claim.x + claim.width for claim in claims)
    fabric_height = max(claim.y + claim.height for claim in claims)

    # fabric[y][x]
    fabric = [[set() for _ in range(fabric_width)]
        for _ in range(fabric_height)]

    for claim in claims:
        add_claim_to_fabric(claim, fabric)

    overlapping_ids = set()

    for x in range(fabric_width):
        for y in range(fabric_height):
            if len(fabric[y][x]) >= 2:
                overlapping_ids |= fabric[y][x]

    for claim in claims:
        if claim.id not in overlapping_ids:
            print(claim.id)


if __name__ == '__main__':
    main()
