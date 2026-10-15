def decimal_to_hexadecimal(n: int) -> str:
    if n < 0:
        return f"-{-n:X}"
    return f"{n:X}"
