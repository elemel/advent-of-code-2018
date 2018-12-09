from sys import stdin


class Link:
    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


def main():
    words = stdin.read().split()
    player_count = int(words[0])
    last_marble = int(words[-2])

    scores = [0 for _ in range(player_count)]
    player = 0
    circle = Link(value=0)
    circle.previous = circle
    circle.next = circle

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            scores[player] += marble

            for i in range(6):
                circle = circle.previous

            scores[player] += circle.previous.value
            circle.previous.previous.next = circle
            circle.previous = circle.previous.previous
        else:
            circle = circle.next
            circle = Link(value=marble, previous=circle, next=circle.next)
            circle.previous.next = circle
            circle.next.previous = circle

        player = (player + 1) % player_count

    print(max(scores))


if __name__ == '__main__':
    main()
