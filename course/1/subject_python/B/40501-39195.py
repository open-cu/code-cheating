def fib(n: int):
    f1, f2 = 1, 1

    for _ in range(n - 1):
        f1, f2 = f2, f1 + f2

    return f1


def solution():
    n = int(input())
    print(fib(n))


solution()
