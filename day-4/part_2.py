from datetime import datetime
from collections import Counter, namedtuple
from operator import attrgetter
from sys import stdin


BeginsShift = namedtuple('BeginsShift', ['timestamp', 'id'])
FallsAsleep = namedtuple('FallsAsleep', ['timestamp'])
WakesUp = namedtuple('WakesUp', ['timestamp'])


def parse_entry(line):
    line = line.strip()
    timestamp = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')

    if 'begins shift' in line:
        id = int(line[26:-13])
        return BeginsShift(timestamp=timestamp, id=id)
    elif 'falls asleep' in line:
        return FallsAsleep(timestamp=timestamp)
    elif 'wakes up' in line:
        return WakesUp(timestamp=timestamp)
    else:
        raise ValueError('Invalid entry line')


def main():
    entries = [parse_entry(line) for line in stdin]
    entries.sort(key=attrgetter('timestamp'))

    id = None
    falls_asleep_minute = None
    scores = Counter()

    for entry in entries:
        if type(entry) is BeginsShift:
            id = entry.id
        elif type(entry) is FallsAsleep:
            falls_asleep_minute = entry.timestamp.minute
        else:
            wakes_up_minute = entry.timestamp.minute

            for minute in range(falls_asleep_minute, wakes_up_minute):
                scores[(id, minute)] += 1

    key, _ = scores.most_common(1)[0]
    id, minute = key
    print(id * minute)


if __name__ == '__main__':
    main()
