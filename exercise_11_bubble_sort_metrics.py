"""Exercise 11: basic Bubble Sort with comparison and swap counts."""

from typing import TypeVar


T = TypeVar("T")

SORTING_METRIC_INPUTS = {
    "already_sorted": [1, 2, 3, 4, 5],
    "reverse": [5, 4, 3, 2, 1],
    "reverse_10": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    "reverse_20": [
        20,
        19,
        18,
        17,
        16,
        15,
        14,
        13,
        12,
        11,
        10,
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1,
    ],
    "mixed": [3, 1, 4, 2, 5],
}


def bubble_sort_metrics(values: list[T]) -> tuple[list[T], int, int]:
    """Return a Bubble-Sorted copy with comparison and swap counts."""
    result = values.copy()
    comparisons = 0
    swaps = 0

    for right in range(len(result) - 1, 0, -1):
        for index in range(right):
            comparisons += 1
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swaps += 1

    return result, comparisons, swaps


def exercise_11_results() -> dict[str, dict[str, object]]:
    """Return basic Bubble Sort metrics for the shared input datasets."""
    results: dict[str, dict[str, object]] = {}
    for dataset_name, values in SORTING_METRIC_INPUTS.items():
        output, comparisons, swaps = bubble_sort_metrics(values)
        results[dataset_name] = {
            "input": values.copy(),
            "output": output,
            "comparisons": comparisons,
            "swaps": swaps,
        }
    return results


def format_exercise_11_evidence() -> str:
    """Format deterministic execution evidence for Exercise 11."""
    lines = ["Exercise 11 — Basic Bubble Sort metrics"]
    for dataset_name, result in exercise_11_results().items():
        lines.append(
            f"{dataset_name}: input={result['input']}; output={result['output']}; "
            f"comparisons={result['comparisons']}; swaps={result['swaps']}"
        )
    return "\n".join(lines)


def main() -> None:
    """Print deterministic execution evidence for Exercise 11."""
    print(format_exercise_11_evidence())


if __name__ == "__main__":
    main()
