n = int(input())

res = []
i = 2
while n > 1:
    if n % i == 0:
        res.append(i)
        n //= i
    elif i > int(n ** 0.5):
        res.append(n)
        break
    else:
        i += 1
print(*sorted(res))
