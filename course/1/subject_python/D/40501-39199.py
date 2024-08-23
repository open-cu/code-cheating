def sign(x):
    return 1 + 2 * (x // (x * x + 1))


def my_abs(x):
    return x * sign(x)


def my_max(a, b):
    return (a + b + my_abs(a - b)) // 2


a = int(input())
b = int(input())
print(my_max(a, b))
