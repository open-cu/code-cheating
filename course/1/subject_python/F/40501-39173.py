n = int(input())
count_divisor = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        count_divisor += 1
        if n // i != i:
            count_divisor += 1
print(count_divisor)
