from collections import deque
from sys import stdin


def main():
    words = stdin.read().split()
    player_count = int(words[0])
    last_marble = int(words[-2])

    scores = player_count * [0]
    player = 0
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            scores[player] += marble
            circle.rotate(7)
            scores[player] += circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(marble)

        player = (player + 1) % player_count

    print(max(scores))


if __name__ == '__main__':
    main()
