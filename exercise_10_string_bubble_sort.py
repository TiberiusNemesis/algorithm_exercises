"""Exercise 10: non-mutating Bubble Sort with lexicographic comparisons."""


def bubble_sort(values: list[str]) -> list[str]:
    """Return a Bubble-Sorted copy of the strings in alphabetical order."""
    result = values.copy()

    for right in range(len(result) - 1, 0, -1):
        for index in range(right):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

    return result


def exercise_10_results() -> dict[str, dict[str, list[str]]]:
    """Return deterministic string sorting demonstrations for distinct inputs."""
    datasets = {
        "Already alphabetical": ["apple", "banana", "orange", "pear"],
        "Unordered": ["pear", "apple", "orange", "banana"],
        "Shared-prefix": ["cat", "car", "can", "cap"],
    }
    return {
        name: {"input": words, "output": bubble_sort(words)}
        for name, words in datasets.items()
    }


def format_exercise_10_evidence() -> str:
    """Format deterministic execution evidence for Exercise 10."""
    lines = ["Exercise 10 — String Bubble Sort"]
    for name, result in exercise_10_results().items():
        lines.append(f"{name} input: {result['input']}")
        lines.append(f"{name} output: {result['output']}")
    return "\n".join(lines)


def main() -> None:
    """Print deterministic execution evidence for Exercise 10."""
    print(format_exercise_10_evidence())


if __name__ == "__main__":
    main()
