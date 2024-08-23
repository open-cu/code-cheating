def div_count(n: int):
    res = 0
    d = 1

    while d * d < n:
        if n % d == 0:
            res += 2
        d += 1

    res += d * d == n

    return res


def solution():
    n = int(input())
    print(div_count(n))


solution()
