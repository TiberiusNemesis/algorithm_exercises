"""Chessboard grain-doubling calculation for Exercise 6."""


def first_square_with_at_least_grains(grain_target: int) -> int | str:
    """Return the first square whose individual grain amount reaches a target.

    If the target is not reachable on an individual square, explain whether it
    remains within the total grains placed across all 64 squares.
    """
    if type(grain_target) is not int:
        raise TypeError("grain target must be a positive integer")
    if grain_target <= 0:
        raise ValueError("grain target must be a positive integer")

    grains_on_square = 1
    total_grains = 0

    for square_number in range(1, 65):
        total_grains += grains_on_square
        if grains_on_square >= grain_target:
            return square_number
        grains_on_square *= 2

    if grain_target > total_grains:
        return "The target exceeds the total grains on the chessboard."

    return "No individual square contains at least the requested number of grains."


def exercise_6_results() -> dict[int, int | str]:
    """Return representative chessboard grain-target results."""
    grain_targets = [1, 2, 4, 8, 1_000, 1_000_000, 2**64]
    return {
        grain_target: first_square_with_at_least_grains(grain_target)
        for grain_target in grain_targets
    }


def format_exercise_6_evidence() -> str:
    """Format deterministic execution evidence for Exercise 6."""
    lines = ["Exercise 6 — Chessboard grain targets"]
    for grain_target, result in exercise_6_results().items():
        lines.append(f"Target {grain_target}: {result}")
    return "\n".join(lines)


def main() -> None:
    """Print deterministic execution evidence for Exercise 6."""
    print(format_exercise_6_evidence())


if __name__ == "__main__":
    main()
