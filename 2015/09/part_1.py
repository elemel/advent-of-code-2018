from sys import stdin


def solve(origin, destinations, distances):
    if not destinations:
        return 0

    return min(
        distances[origin, destination] +
        solve(destination, destinations[:i] + destinations[i + 1:], distances)
        for i, destination in enumerate(destinations))


def main():
    distances = {}

    for line in stdin:
        origin, _, destination, _, distance_str = line.strip().split()
        distance = int(distance_str)

        distances[origin, destination] = distance
        distances[destination, origin] = distance

    locations = list({origin for origin, _ in distances})

    shortest_distance = min(
        solve(origin, locations[:i] + locations[i + 1:], distances)
        for i, origin in enumerate(locations))

    print(shortest_distance)


if __name__ == '__main__':
    main()
