def linear_search(records, target):
    for i, value in enumerate(records):
        if value == target:
            return i
    return -1


def recursive_binary_search(records, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if records[mid] == target:
        return mid
    if target < records[mid]:
        return recursive_binary_search(records, target, low, mid - 1)
    return recursive_binary_search(records, target, mid + 1, high)


def build_hash_table(records):
    # Registration numbers are unique in this scenario.
    return {value: value for value in records}


def hash_search(table, target):
    return table.get(target)  # None means not found


def run_correctness_tests():
    values = [192466003, 192466001, 192466002, 192466004]
    target = 192466002

    assert linear_search(values, target) == 2

    ordered = sorted(values)
    result_index = recursive_binary_search(
        ordered, target, 0, len(ordered) - 1
    )
    assert result_index != -1 and ordered[result_index] == target

    table = build_hash_table(values)
    assert hash_search(table, target) == target

    # Missing-key and boundary tests
    missing = 999999999
    assert linear_search(values, missing) == -1
    assert recursive_binary_search(
        ordered, missing, 0, len(ordered) - 1
    ) == -1
    assert hash_search(table, missing) is None

    assert linear_search([], target) == -1
    assert recursive_binary_search([], target, 0, -1) == -1
    assert hash_search({}, target) is None
    return "All correctness tests passed"
