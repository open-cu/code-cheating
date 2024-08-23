def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_n(lst):
    if len(lst) == 1:
        return lst[0]
    res = gcd(lst[0], lst[1])
    for i in range(2, len(lst)):
        res = gcd(res, lst[i])
    return res


n = int(input())
lst = list(map(int, input().split()))
print(gcd_n(lst))
