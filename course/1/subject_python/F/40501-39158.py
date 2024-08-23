n = int(input())


def check_divisibility(n):
    total = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            total += 2
            if i == n // i:
                total -= 1
    return total


print(check_divisibility(n))
