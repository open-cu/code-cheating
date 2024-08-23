def is_even(n: int):
    while n > 0:
        if n % 2 == 1:
            return False
        n //= 10
    return True


def even_count(n: int):
    res = 0

    for d in range(2, n + 1, 2):
        if is_even(d):
            res += 1

    return res


def solution():
    n = int(input())
    print(even_count(n))


solution()
