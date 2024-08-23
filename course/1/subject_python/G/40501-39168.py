n = int(input())


def simple_delitels(n):
    s_delitels = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            s_delitels.append(str(d))
            n //= d
        else:
            d += 1
    if n > 1:
        s_delitels.append(str(n))
    return s_delitels


lst_dels = simple_delitels(n)

print(' '.join(lst_dels))
