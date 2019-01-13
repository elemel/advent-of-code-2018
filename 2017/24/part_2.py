from collections import deque
from sys import stdin


def main():
    components = [tuple(int(s) for s in line.split('/')) for line in stdin]
    queue = deque([(0, 0, 0, 0)])
    visited = set()
    max_length = 0
    max_strength = 0

    while queue:
        key = queue.popleft()

        if key in visited:
            continue

        visited.add(key)
        used, length, strength, port = key

        if length == max_length:
            max_strength = max(strength, max_strength)
        elif length > max_length:
            max_length = length
            max_strength = strength

        for i, component in enumerate(components):
            if used & (1 << i):
                continue

            if port not in component:
                continue

            port_1, port_2 = component

            new_used = used | (1 << i)
            new_length = length + 1
            new_strength = strength + sum(component)
            new_port = port_2 if port == port_1 else port_1

            queue.append((new_used, new_length, new_strength, new_port))

    print(max_strength)


if __name__ == '__main__':
    main()
