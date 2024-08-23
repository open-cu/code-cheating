def func(n, nonzero):
    # 0 -> 0
    # !0 -> 1
    # nonzero as argument to avoid use constant(1)
    # (n-n) - expr  = -expr to avoid use -expr cause unary '-' may be not allowed, only binary: expr1 - expr2
    return (n - n) - ((-n * n) // (n * n + nonzero // nonzero))


def func2(lhs, rhs):
    # if a == b, return 2
    # if a != b, return 1
    # 2 - func(a - b, a)
    return (lhs + lhs) // lhs - func(lhs - rhs, lhs)


a = int(input())
b = int(input())
res = (a * func(a // b, a) + b * func(b // a, a)) // func2(a, b)

print(res)
