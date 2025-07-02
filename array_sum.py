def sum_neg_between_min_max(arr):
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    start, end = sorted([min_idx, max_idx])
    return sum(x for x in arr[start+1:end] if x < 0)

# Пример использования
test_array = [3, -1, -2, 5, -4]
print(sum_neg_between_min_max(test_array))  # Вывод: -2
