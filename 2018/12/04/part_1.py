from datetime import datetime
from collections import Counter, defaultdict, namedtuple
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
    guard_scores = Counter()
    guard_entries = defaultdict(list)

    for entry in entries:
        if type(entry) is BeginsShift:
            id = entry.id
        else:
            if type(entry) is WakesUp:
                falls_asleep_minute = guard_entries[id][-1].timestamp.minute
                wakes_up_minute = entry.timestamp.minute
                guard_scores[id] += wakes_up_minute - falls_asleep_minute

            guard_entries[id].append(entry)

    winner_id, _ = guard_scores.most_common(1)[0]
    winner_entries = guard_entries[winner_id]
    minute_scores = Counter()

    for i in range(0, len(winner_entries), 2):
        falls_asleep_minute = winner_entries[i].timestamp.minute
        wakes_up_minute = winner_entries[i + 1].timestamp.minute

        for minute in range(falls_asleep_minute, wakes_up_minute):
            minute_scores[minute] += 1

    winner_minute, _ = minute_scores.most_common(1)[0]
    print(winner_id * winner_minute)


if __name__ == '__main__':
    main()
