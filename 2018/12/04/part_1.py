from collections import Counter, defaultdict
from sys import stdin


def parse_guard_id(line):
    return int(line[26:-13])


def parse_minute(line):
    return int(line[15:17])


def main():
    lines = sorted(line.strip() for line in stdin)

    guard_id = None
    falls_asleep_minute = None

    guard_counter = Counter()
    guard_minute_counters = defaultdict(Counter)

    for line in lines:
        if line.endswith(' begins shift'):
            guard_id = parse_guard_id(line)
        elif line.endswith(' falls asleep'):
            falls_asleep_minute = parse_minute(line)
        elif line.endswith(' wakes up'):
            wakes_up_minute = parse_minute(line)
            guard_counter[guard_id] += wakes_up_minute - falls_asleep_minute

            for minute in range(falls_asleep_minute, wakes_up_minute):
                guard_minute_counters[guard_id][minute] += 1

    (guard_id, _), = guard_counter.most_common(1)
    (minute, _), = guard_minute_counters[guard_id].most_common(1)
    print(guard_id * minute)


if __name__ == '__main__':
    main()
