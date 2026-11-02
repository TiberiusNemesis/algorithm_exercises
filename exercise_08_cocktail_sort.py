"""Exercise 8: bidirectional Bubble Sort using left and right bounds."""

from typing import TypeVar


T = TypeVar("T")


def cocktail_sort(values: list[T]) -> list[T]:
    """Return a non-mutating Cocktail-Sorted copy of ``values``."""
    result = values.copy()
    left = 0
    right = len(result) - 1

    while left < right:
        for index in range(left, right):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

        right -= 1

        for index in range(right, left, -1):
            if result[index - 1] > result[index]:
                result[index - 1], result[index] = result[index], result[index - 1]

        left += 1

    return result


def exercise_8_results() -> dict[str, dict[str, list[int]]]:
    """Return deterministic Cocktail Sort demonstrations for distinct inputs."""
    test_cases = {
        "Already sorted": [1, 2, 3, 4, 5],
        "Reverse-order": [5, 4, 3, 2, 1],
        "Mixed": [3, 4, 5, 1, 2, 3],
    }
    return {
        name: {"input": values, "output": cocktail_sort(values)}
        for name, values in test_cases.items()
    }


def format_exercise_8_evidence() -> str:
    """Format deterministic execution evidence for Exercise 8."""
    lines = ["Exercise 8 — Cocktail Sort"]
    for name, result in exercise_8_results().items():
        lines.append(f"{name} input: {result['input']}")
        lines.append(f"{name} output: {result['output']}")
    return "\n".join(lines)


def main() -> None:
    """Print deterministic execution evidence for Exercise 8."""
    print(format_exercise_8_evidence())


if __name__ == "__main__":
    main()
