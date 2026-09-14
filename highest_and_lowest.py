def high_and_low(numbers: str) -> str:
    numbers = [int(digit) for digit in numbers.split()]
    return f"{max(numbers)} {min(numbers)}"
