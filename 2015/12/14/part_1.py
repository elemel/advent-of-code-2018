from sys import stdin


def parse_reindeer(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    speed, flying_time, resting_time = [int(s) for s in number_line.split()]
    return speed, flying_time, resting_time


def get_distance(reindeer, t):
    speed, flying_time, resting_time = reindeer
    q, r = divmod(t, flying_time + resting_time)
    total_flying_time = q * flying_time + min(r, flying_time)
    return speed * total_flying_time


def main():
    reindeer_list = [parse_reindeer(line.strip()) for line in stdin]
    print(max(get_distance(reindeer, 2503) for reindeer in reindeer_list))


if __name__ == '__main__':
    main()
