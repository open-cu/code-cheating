n = int(input())
i = 1
divisors = 0
while i ** 2 <= n:
    if i**2 == n:
        divisors += 1
    elif n % i == 0 and i**2 != n:
        divisors += 2
    i += 1
print(divisors)