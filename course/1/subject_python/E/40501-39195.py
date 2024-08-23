def is_prime(n: int):
    if n != 2 and n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def solution():
    n = int(input())
    print("prime" if is_prime(n) else "composite")


solution()
