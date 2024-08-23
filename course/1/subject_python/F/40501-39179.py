def divisors_number(n):
    if n == 1:
        return 1
    res = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
    res.append(n)
    length = len(res)

    for a in range(length):
        for b in range(a, length):
            if n % (res[a] * res[b]) == 0 and res[a] * res[b] not in res:
                res.append(res[a] * res[b])
            if n % (res[b] // res[a]) == 0 and res[b] // res[a] not in res:
                res.append(res[b] // res[a])
    return len(res)


n = int(input())
print(divisors_number(n))