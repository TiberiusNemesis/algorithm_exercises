"""Exercise 13: deterministic comparison of linear and binary search costs."""

import random


def linear_search_count(arr: list[int], target: int) -> tuple[int, int]:
    """Return the target index and the number of evaluated key comparisons."""
    comparisons = 0
    for index in range(len(arr)):
        comparisons += 1
        if arr[index] == target:
            return index, comparisons
    return -1, comparisons


def binary_search_count(sorted_arr: list[int], target: int) -> tuple[int, int]:
    """Return the target index and every evaluated binary-search key comparison.

    Each loop counts the equality comparison. A failed equality comparison also
    counts the direction comparison used to choose the next half of the list.
    """
    low = 0
    high = len(sorted_arr) - 1
    comparisons = 0

    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if sorted_arr[middle] == target:
            return middle, comparisons

        comparisons += 1
        if sorted_arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1, comparisons


def bubble_sort_count(arr: list[int]) -> tuple[list[int], int]:
    """Return an unoptimized Bubble-Sorted copy and every adjacent comparison."""
    result = arr.copy()
    comparisons = 0

    for right in range(len(result) - 1, 0, -1):
        for index in range(right):
            comparisons += 1
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

    return result, comparisons


def _exercise_13_datasets() -> dict[str, list[int]]:
    """Build the three required 31-item inputs in a fixed order."""
    arr_sorted = list(range(1, 32))
    arr_reverse = arr_sorted[::-1]
    arr_random = arr_sorted.copy()
    random.seed(42)
    random.shuffle(arr_random)

    return {
        "arr_sorted": arr_sorted,
        "arr_reverse": arr_reverse,
        "arr_random": arr_random,
    }


def _exercise_13_target_result(
    original_values: list[int], target: int, is_already_sorted: bool
) -> dict[str, int]:
    """Measure one target without reusing preprocessing from another target."""
    linear_index, linear_comparisons = linear_search_count(original_values, target)

    if is_already_sorted:
        sorted_values = original_values.copy()
        bubble_sort_comparisons = 0
    else:
        sorted_values, bubble_sort_comparisons = bubble_sort_count(original_values)

    binary_index, binary_comparisons = binary_search_count(sorted_values, target)
    return {
        "target": target,
        "linear_index": linear_index,
        "linear_comparisons": linear_comparisons,
        "binary_index": binary_index,
        "binary_comparisons": binary_comparisons,
        "bubble_sort_comparisons": bubble_sort_comparisons,
        "bubble_sort_plus_binary_comparisons": (
            bubble_sort_comparisons + binary_comparisons
        ),
    }


def exercise_13_results() -> dict[str, dict[str, dict[str, int]]]:
    """Compare linear and binary search counts on the required original inputs."""
    results: dict[str, dict[str, dict[str, int]]] = {}

    for dataset_name, original_values in _exercise_13_datasets().items():
        targets = {
            "target_first": original_values[0],
            "target_middle": original_values[31 // 2],
            "target_absent": -1,
        }
        is_already_sorted = dataset_name == "arr_sorted"
        results[dataset_name] = {
            target_name: _exercise_13_target_result(
                original_values, target, is_already_sorted
            )
            for target_name, target in targets.items()
        }

    return results


def format_exercise_13_evidence() -> str:
    """Format deterministic execution evidence for Exercise 13."""
    lines = ["Exercise 13 — Search comparison counts"]
    exercise_13_inputs = _exercise_13_datasets()
    for dataset_name, target_results in exercise_13_results().items():
        lines.append(
            f"{dataset_name} original order: {exercise_13_inputs[dataset_name]}"
        )
        for target_name, result in target_results.items():
            lines.append(
                f"{target_name}: target={result['target']}; "
                f"linear index={result['linear_index']}; "
                f"linear comparisons={result['linear_comparisons']}; "
                f"binary index={result['binary_index']}; "
                f"binary comparisons={result['binary_comparisons']}; "
                f"Bubble Sort comparisons={result['bubble_sort_comparisons']}; "
                "Bubble Sort plus binary comparisons="
                f"{result['bubble_sort_plus_binary_comparisons']}"
            )
    return "\n".join(lines)


def main() -> None:
    """Print deterministic execution evidence for Exercise 13."""
    print(format_exercise_13_evidence())


if __name__ == "__main__":
    main()
