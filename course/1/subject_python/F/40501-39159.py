n = int(input())

divisor_count = 1 + (n > 1)
i = 2
while (i * i < n):
    if (n % i == 0):
        divisor_count += 2
    i += 1
if (i * i == n):
    divisor_count += 1

print(divisor_count)
