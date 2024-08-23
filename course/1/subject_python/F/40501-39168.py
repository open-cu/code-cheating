n = int(input())


def simple_delitels(n):
    s_delitels = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            s_delitels.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        s_delitels.append(n)
    return s_delitels


lst_dels = simple_delitels(n)

num_dels = 1

for i in set(lst_dels):
    num_dels *= lst_dels.count(i) + 1

print(num_dels)
