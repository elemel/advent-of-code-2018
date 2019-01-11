from collections import deque
from sys import stdin


def main():
    step_count = int(stdin.read().strip())
    circular_buffer = deque([0])

    for i in range(1, 50_000_001):
        circular_buffer.rotate(-step_count)
        circular_buffer.append(i)

    i = circular_buffer.index(0)
    print(circular_buffer[(i + 1) % 50_000_001])


if __name__ == '__main__':
    main()
