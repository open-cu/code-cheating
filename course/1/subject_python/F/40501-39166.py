def count_divisors(n):
    divisors = 0
    sqrt_n = int(n**0.5)

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors += 2

    if sqrt_n * sqrt_n == n:
        divisors -= 1

    return divisors


n = int(input())


result = count_divisors(n)
print(result)
