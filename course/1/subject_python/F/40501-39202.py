import math
num = int(input(''))
divisors = 0

# Если число полный квадрат, то вычитаем 1 делитель
sqrt = int(math.sqrt(num))
if num - sqrt ** 2 == 0:
    divisors -= 1

for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        divisors += 2
print(divisors)
