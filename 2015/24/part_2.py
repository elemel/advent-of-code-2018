from sys import maxsize, stdin


def solve(
    packages,
    package_index,
    balanced_weight,
    group_1,
    group_2,
    group_3,
    group_4,
    package_count,
    quantum_entanglement,
    seen):

    if (seen.get((group_1, group_2, group_3, group_4), (maxsize, maxsize)) <=
        (package_count, quantum_entanglement)):

        return maxsize, maxsize

    seen[group_1, group_2, group_3, group_4] = (
        package_count, quantum_entanglement)

    if package_index == len(packages):
        return package_count, quantum_entanglement

    package_weight = packages[package_index]
    result = maxsize, maxsize

    if group_1 + package_weight <= balanced_weight:
        result = min(
            result,
            solve(
                packages,
                package_index + 1,
                balanced_weight,
                group_1 + package_weight,
                group_2,
                group_3,
                group_4,
                package_count + 1,
                quantum_entanglement * package_weight,
                seen))

    if group_2 + package_weight <= balanced_weight:
        sorted_groups = sorted([group_2 + package_weight, group_3, group_4])

        result = min(
            result,
            solve(
                packages,
                package_index + 1,
                balanced_weight,
                group_1,
                sorted_groups[0],
                sorted_groups[1],
                sorted_groups[2],
                package_count,
                quantum_entanglement,
                seen))

    if group_3 + package_weight <= balanced_weight:
        result = min(
            result,
            solve(
                packages,
                package_index + 1,
                balanced_weight,
                group_1,
                group_2,
                min(group_3 + package_weight, group_4),
                max(group_3 + package_weight, group_4),
                package_count,
                quantum_entanglement,
                seen))

    if group_4 + package_weight <= balanced_weight:
        result = min(
            result,
            solve(
                packages,
                package_index + 1,
                balanced_weight,
                group_1,
                group_2,
                group_3,
                group_4 + package_weight,
                package_count,
                quantum_entanglement,
                seen))

    return result


def main():
    packages = [int(line.strip()) for line in stdin]
    packages.sort()
    packages.reverse()
    balanced_weight = sum(packages) // 4

    _, quantum_entanglement = solve(
        packages, 0, balanced_weight, 0, 0, 0, 0, 0, 1, {})

    print(quantum_entanglement)


if __name__ == '__main__':
    main()
