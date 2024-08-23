import math

n = int(input())
dividers = 0
sqrt_n = int(math.sqrt(n))

for i in range(1, sqrt_n + 1):
    if n % i == 0:

        dividers += 1
        if i != n // i:
            dividers += 1
print(dividers)
