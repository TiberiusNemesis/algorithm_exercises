"""Exercise 5: find the largest unique integer in linear time."""


def largest_unique_value(values: list[int]) -> int | None:
    """Return the largest value that occurs exactly once, if one exists."""
    frequencies: dict[int, int] = {}
    for value in values:
        frequencies[value] = frequencies.get(value, 0) + 1

    largest_value: int | None = None
    for value in values:
        if frequencies[value] == 1 and (
            largest_value is None or value > largest_value
        ):
            largest_value = value

    return largest_value


def exercise_5_result() -> int | None:
    """Return the largest unique value for a reproducible input."""
    return largest_unique_value([5, 1, 5, 3, 2, 2])


def format_exercise_5_evidence() -> str:
    """Format deterministic execution evidence for Exercise 5."""
    return "\n".join(
        (
            "Exercise 5 — Largest unique value",
            f"Largest unique value: {exercise_5_result()}",
        )
    )


def main() -> None:
    """Print deterministic execution evidence for Exercise 5."""
    print(format_exercise_5_evidence())


if __name__ == "__main__":
    main()
