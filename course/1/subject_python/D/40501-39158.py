n_1 = int(input())
n_2 = int(input())


def check_maximum(a, b):
    c = a // b
    c = ((c + 2) // (c + 1)) % 2
    d = (c + 1) % 2
    res = a * c + b * d
    return res


print(check_maximum(n_1, n_2))
