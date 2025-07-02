def max_dragon_power(N):
    if N <= 4:
        return N
    power = 1
    while N > 4:
        power *= 3
        N -= 3
    return power * N

# Тесты
print(max_dragon_power(5))  # Вывод: 6
print(max_dragon_power(8))  # Вывод: 18
print(max_dragon_power(10)) # Вывод: 36
