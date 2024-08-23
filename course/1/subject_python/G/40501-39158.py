n = int(input())


def factorization(n):
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            result.append(i)
            n //= i

    if n > 2:
        result.append(n)

    return result


print(*factorization(n))