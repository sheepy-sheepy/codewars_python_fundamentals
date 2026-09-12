def array_diff(a: list[int], b: list[int]) -> list[int]:
    return [digit for digit in a if digit not in b]
