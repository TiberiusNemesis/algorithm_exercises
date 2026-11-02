"""Exercise 9: non-mutating numeric Bubble Sort."""


def bubble_sort_count(values: list[int]) -> tuple[list[int], int]:
    """Return a Bubble-Sorted copy and every adjacent comparison."""
    result = values.copy()
    comparisons = 0

    for right in range(len(result) - 1, 0, -1):
        for index in range(right):
            comparisons += 1
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

    return result, comparisons


def bubble_sort(values: list[int]) -> list[int]:
    """Return a non-mutating Bubble-Sorted copy of the numbers."""
    result, _ = bubble_sort_count(values)
    return result


def exercise_9_results() -> dict[str, dict[str, object]]:
    """Return numeric sorting evidence for sorted and unordered inputs."""
    datasets = {
        "already_sorted": [1, 2, 3, 4],
        "unordered": [5, 1, 4, 2, 8],
    }
    results: dict[str, dict[str, object]] = {}
    for dataset_name, values in datasets.items():
        output, comparisons = bubble_sort_count(values)
        results[dataset_name] = {
            "input": values,
            "output": output,
            "comparisons": comparisons,
        }
    return results


def format_exercise_9_evidence() -> str:
    """Format deterministic execution evidence for Exercise 9."""
    lines = ["Exercise 9 — Numeric Bubble Sort"]
    for dataset_name, result in exercise_9_results().items():
        lines.append(
            f"{dataset_name}: input={result['input']}; output={result['output']}; "
            f"adjacent comparisons={result['comparisons']}"
        )
    return "\n".join(lines)


def main() -> None:
    """Print deterministic execution evidence for Exercise 9."""
    print(format_exercise_9_evidence())


if __name__ == "__main__":
    main()
