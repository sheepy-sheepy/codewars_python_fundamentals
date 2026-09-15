def find_it(seq: list[int]) -> int:
    result = 0
    for digit in seq:
        result ^= digit
    return result
