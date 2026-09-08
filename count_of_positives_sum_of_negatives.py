def count_positives_sum_negatives(arr: list[int]) -> list[int]:
    count_positives = sum(1 for num in arr if num > 0)
    sum_negatives = sum(num for num in arr if num < 0)
    return [count_positives, sum_negatives] if arr else []


print(count_positives_sum_negatives([]))
