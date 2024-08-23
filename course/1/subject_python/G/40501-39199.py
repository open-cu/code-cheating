def prime_factorize(n):
    res = []
    k = 2

    while k * k <= n:
        if n % k == 0:
            res.append(k)
            n //= k
        else:
            k += 1

    if n > 1:
        res.append(n)

    return res


n = int(input())
print(*prime_factorize(n))
