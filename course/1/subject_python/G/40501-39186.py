def factorization(n):
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res


n = int(input())
print(*factorization(n), sep=' ')
