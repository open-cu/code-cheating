def fib(n: int) -> int:
    a, b, c, d = (1, 1, 1, 0)
    rc, rd = (0, 1)

    while n > 0:
        if n % 2 != 0:
            rc, rd = (
                rc*a + rd*c,
                rc*b + rd*d
            )

        a, b, c, d = (
            a*a + b*c,
            a*b + b*d,
            c*a + d*c,
            c*b + d*d
        )
        n = n//2
    return rc


n = int(input())
print(fib(n))
