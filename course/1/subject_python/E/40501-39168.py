a = int(input())


def make_delitels(num):
    delitels = []
    delitels.append(1)
    if num > 1:
        delitels.append(num)
    i = 2
    while i * i <= num:
        if num % i == 0:
            delitels.append(i)
            num //= i
        else:
            i += 1
    return delitels


lst_dels = make_delitels(a)

if len(lst_dels) <= 2:
    print('prime')
else:
    print('composite')
