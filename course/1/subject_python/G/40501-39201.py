def is_composite(n):
    a = 3
    while a**2 <= n and n % a != 0:
        a += 2
    return 0 if a**2 > n else 1


n = int(input())
quotients = []

while n != 1:
    if n % 2 == 0:
        quotients.append(2)
        n = n // 2
    elif is_composite(n) == 0:
        quotients.append(n)
        n = 1
        break
    else:
        odd = 3
        while odd <= n:
            if n % odd == 0:
                quotients.append(odd)
                n = n // odd
                break
            else:
                odd += 2
quotients.sort()
print(' '.join(map(str, quotients)))
