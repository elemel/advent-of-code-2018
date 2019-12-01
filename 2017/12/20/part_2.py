from itertools import groupby
from operator import itemgetter
from sys import stdin


def parse_particle(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    x, y, z, vx, vy, vz, ax, ay, az = [int(s) for s in number_line.split()]
    return (x, y, z), (vx, vy, vz), (ax, ay, az)


def main():
    particles = [parse_particle(line.strip()) for line in stdin]

    for _ in range(10_000):
        particles.sort()

        collisions = [
            list(collision)
            for _, collision in groupby(particles, itemgetter(0))
        ]

        particles = [
            particle
            for collision in collisions
            if len(collision) == 1
            for particle in collision
        ]

        for i in range(len(particles)):
            (x, y, z), (vx, vy, vz), (ax, ay, az) = particles[i]

            vx += ax
            vy += ay
            vz += az

            x += vx
            y += vy
            z += vz

            particles[i] = (x, y, z), (vx, vy, vz), (ax, ay, az)

    print(len(particles))


if __name__ == '__main__':
    main()
