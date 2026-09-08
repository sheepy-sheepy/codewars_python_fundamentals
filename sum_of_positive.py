def positive_sum(arr):
    sum_arr = 0
    for num in arr:
        if num <= 0:
            continue
        sum_arr += num
    return sum_arr


print(positive_sum([1, -4, 7, 12]))
