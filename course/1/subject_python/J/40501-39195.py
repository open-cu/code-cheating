from functools import reduce


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def solution():
    input()
    arr = [int(i) for i in input().split()]

    res = reduce(lambda a, b: gcd(a, b), arr)
    print(res)


solution()
