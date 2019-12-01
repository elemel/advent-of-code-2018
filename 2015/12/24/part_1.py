from sys import maxsize, stdin


def solve(
    packages,
    package_index,
    balanced_weight,
    groups,
    stats,
    seen):

    if stats >= seen.get(groups, (maxsize, maxsize)):
        return maxsize, maxsize

    seen[groups] = stats

    if package_index == len(packages):
        return stats

    package_weight = packages[package_index]
    result = maxsize, maxsize
    group_1, group_2, group_3 = groups

    if group_1 + package_weight <= balanced_weight:
        package_count, quantum_entanglement = stats

        result = min(
            result,
            solve(
                packages,
                package_index + 1,
                balanced_weight,
                (group_1 + package_weight, group_2, group_3),
                (package_count + 1, quantum_entanglement * package_weight),
                seen))

    if group_2 + package_weight <= balanced_weight:
        new_group_2, new_group_3 = sorted([group_2 + package_weight, group_3])

        result = min(
            result,
            solve(
                packages,
                package_index + 1,
                balanced_weight,
                (group_1, new_group_2, new_group_3),
                stats,
                seen))

    if group_3 + package_weight <= balanced_weight:
        result = min(
            result,
            solve(
                packages,
                package_index + 1,
                balanced_weight,
                (group_1, group_2, group_3 + package_weight),
                stats,
                seen))

    return result


def main():
    packages = [int(line.strip()) for line in stdin]
    packages.sort()
    packages.reverse()
    balanced_weight = sum(packages) // 3

    _, quantum_entanglement = solve(
        packages, 0, balanced_weight, (0, 0, 0), (0, 1), {})

    print(quantum_entanglement)


if __name__ == '__main__':
    main()
