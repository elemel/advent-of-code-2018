from collections import deque
from sys import stdin


def main():
    step_count = int(stdin.read().strip())
    circular_buffer = deque([0])

    for i in range(1, 2018):
        circular_buffer.rotate(-step_count)
        circular_buffer.append(i)

    print(circular_buffer[0])


if __name__ == '__main__':
    main()
