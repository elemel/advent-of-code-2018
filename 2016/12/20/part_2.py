from sys import stdin


def parse_ip_range(line):
    start, end = [int(s) for s in line.split('-')]
    return start, end


def main():
    blocked_ip_ranges = [parse_ip_range(line.strip()) for line in stdin]
    blocked_ip_ranges.sort()
    blocked_ip_ranges.reverse()

    ip = 0
    allowed_ip_count = 0

    while blocked_ip_ranges:
        start, end = blocked_ip_ranges.pop()

        if ip < start:
            allowed_ip_count += start - ip

        ip = max(ip, end + 1)

    allowed_ip_count += 4294967296 - ip
    print(allowed_ip_count)


if __name__ == '__main__':
    main()
