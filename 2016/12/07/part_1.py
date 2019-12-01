from sys import stdin


def split_ip(ip):
    j = 0

    for i, c in enumerate(ip):
        if c in '[]':
            yield ip[j:i]
            j = i + 1

    yield ip[j:]


def contains_abba(ip):
    return any(
        ip[i + 1] != ip[i] and ip[i + 2] == ip[i + 1] and ip[i + 3] == ip[i]
        for i in range(len(ip) - 3))


def supports_tls(ip):
    result = False

    for i, part in enumerate(split_ip(ip)):
        if contains_abba(part):
            if i % 2 == 0:
                result = True
            else:
                return False

    return result


def main():
    ips = [line.strip() for line in stdin]
    print(sum(supports_tls(ip) for ip in ips))


if __name__ == '__main__':
    main()
