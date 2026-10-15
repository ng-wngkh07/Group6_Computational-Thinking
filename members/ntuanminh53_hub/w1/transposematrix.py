def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Return the transpose of a matrix without modifying the original."""
    if not matrix:
        return []

    return [list(row) for row in zip(*matrix)]