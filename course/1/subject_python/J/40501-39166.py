import math

# Считываем количество чисел
n = int(input())

# Считываем n чисел и разделяем их по пробелам
numbers = list(map(int, input().split()))

# Если введено только одно число, то оно и будет НОД
if n == 1:
    gcd_result = numbers[0]
else:
    # Инициализируем НОД первых двух чисел
    gcd_result = math.gcd(numbers[0], numbers[1])

    # Находим НОД для остальных чисел
    for i in range(2, n):
        gcd_result = math.gcd(gcd_result, numbers[i])

# Выводим результат
print(gcd_result)
