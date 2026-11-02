"""Exercise 14: readable refactorings that preserve the supplied behavior."""


def binary_search_with_count(values: list[int], target: int) -> tuple[int, int]:
    """Return a binary-search index and the supplied comparison count."""
    lower_bound = 0
    upper_bound = len(values) - 1
    comparisons = 0

    while lower_bound <= upper_bound:
        middle_index = (lower_bound + upper_bound) // 2
        comparisons += 1
        if values[middle_index] == target:
            return middle_index, comparisons

        # Preserve the supplied algorithm's second count after every miss.
        comparisons += 1
        if target < values[middle_index]:
            upper_bound = middle_index - 1
        else:
            lower_bound = middle_index + 1

    return -1, comparisons


def bubble_sort_with_count(values: list[int]) -> tuple[list[int], int]:
    """Return a copied Bubble-Sorted list and all adjacent comparisons."""
    result = values.copy()
    comparisons = 0

    for right_bound in range(len(result) - 1, 0, -1):
        for index in range(right_bound):
            comparisons += 1
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
        # Preserve the supplied full-pass behavior; do not add an early exit.

    return result, comparisons


def _provided_binary_search(values: list[int], target: int) -> tuple[int, int]:
    """Run the supplied pre-refactoring binary search for comparison only."""
    comparisons = 0
    lower_bound = 0
    upper_bound = len(values) - 1
    result_index = -1

    while lower_bound <= upper_bound:
        middle_index = (lower_bound + upper_bound) // 2
        comparisons += 1
        if values[middle_index] == target:
            result_index = middle_index
            break
        comparisons += 1
        if target < values[middle_index]:
            upper_bound = middle_index - 1
        else:
            lower_bound = middle_index + 1

    return result_index, comparisons


def _provided_bubble_sort(values: list[int]) -> tuple[list[int], int]:
    """Run the supplied pre-refactoring Bubble Sort for comparison only."""
    result = values[:]
    comparisons = 0

    for right_bound in range(len(result) - 1, 0, -1):
        for index in range(right_bound):
            comparisons += 1
            if result[index] > result[index + 1]:
                temporary_value = result[index]
                result[index] = result[index + 1]
                result[index + 1] = temporary_value

    return result, comparisons


def refactoring_preserves_behavior() -> bool:
    """Check representative results against the supplied original algorithms."""
    search_values = [2, 4, 6, 8, 10, 12, 13]
    search_targets = [2, 8, 9, 13, 14]
    sorting_inputs = [
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 4, 2, 5],
        [],
        [7],
    ]

    searches_match = all(
        binary_search_with_count(search_values, target)
        == _provided_binary_search(search_values, target)
        for target in search_targets
    )
    sorts_match = all(
        bubble_sort_with_count(values) == _provided_bubble_sort(values)
        for values in sorting_inputs
    )
    return searches_match and sorts_match


def exercise_14_results() -> dict[str, object]:
    """Return representative deterministic results for the refactored code."""
    search_values = [2, 4, 6, 8, 10, 12, 13]
    sorting_values = [1, 2, 3, 4]
    reverse_values = [4, 3, 2, 1]

    return {
        "binary_found": binary_search_with_count(search_values, 8),
        "binary_absent": binary_search_with_count(search_values, 9),
        "bubble_sorted": bubble_sort_with_count(sorting_values),
        "bubble_reverse": bubble_sort_with_count(reverse_values),
        "behavior_preserved": refactoring_preserves_behavior(),
    }


def format_exercise_14_evidence() -> str:
    """Format representative behavior evidence for Exercise 14."""
    results = exercise_14_results()
    return "\n".join(
        (
            "Exercise 14 — Behavior-preserving refactoring",
            "Binary search found: "
            f"index={results['binary_found'][0]}; comparisons={results['binary_found'][1]}",
            "Binary search absent: "
            f"index={results['binary_absent'][0]}; comparisons={results['binary_absent'][1]}",
            "Bubble Sort sorted: "
            f"output={results['bubble_sorted'][0]}; comparisons={results['bubble_sorted'][1]}",
            "Bubble Sort reverse: "
            f"output={results['bubble_reverse'][0]}; comparisons={results['bubble_reverse'][1]}",
            "Behavior preservation check: "
            f"passed={results['behavior_preserved']}",
        )
    )


def main() -> None:
    """Print representative behavior evidence for Exercise 14."""
    print(format_exercise_14_evidence())


if __name__ == "__main__":
    main()
