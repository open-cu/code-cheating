from functools import reduce


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


n = input()
print(reduce(gcd, map(int, input().split())))
