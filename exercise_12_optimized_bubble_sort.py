"""Exercise 12: instrumented Bubble Sort with an early exit after no swaps."""

from typing import TypeVar

if __package__:
    from .exercise_11_bubble_sort_metrics import SORTING_METRIC_INPUTS
else:
    from exercise_11_bubble_sort_metrics import SORTING_METRIC_INPUTS


T = TypeVar("T")


def optimized_bubble_sort_metrics(values: list[T]) -> tuple[list[T], int, int]:
    """Return a Bubble-Sorted copy, ending after a no-swap pass."""
    result = values.copy()
    comparisons = 0
    swaps = 0

    for right in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(right):
            comparisons += 1
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return result, comparisons, swaps


def exercise_12_results() -> dict[str, dict[str, object]]:
    """Return optimized metrics for the same inputs used by Exercise 11."""
    results: dict[str, dict[str, object]] = {}
    for dataset_name, values in SORTING_METRIC_INPUTS.items():
        output, comparisons, swaps = optimized_bubble_sort_metrics(values)
        results[dataset_name] = {
            "input": values.copy(),
            "output": output,
            "comparisons": comparisons,
            "swaps": swaps,
        }
    return results


def format_exercise_12_evidence() -> str:
    """Format deterministic execution evidence for Exercise 12."""
    lines = ["Exercise 12 — Optimized Bubble Sort metrics"]
    for dataset_name, result in exercise_12_results().items():
        lines.append(
            f"{dataset_name}: input={result['input']}; output={result['output']}; "
            f"comparisons={result['comparisons']}; swaps={result['swaps']}"
        )
    return "\n".join(lines)


def main() -> None:
    """Print deterministic execution evidence for Exercise 12."""
    print(format_exercise_12_evidence())


if __name__ == "__main__":
    main()
