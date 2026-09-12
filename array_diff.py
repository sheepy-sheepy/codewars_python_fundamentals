def array_diff(a: list[int], b: list[int]) -> list[int]:
    diff_digits = list(set(a).difference(set(b)))
    return [digit for digit in a if digit in diff_digits]


print(array_diff([1, 2, 2], [1]))
