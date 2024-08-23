n = int(input())
mul = 2
multipliers = []
while mul * mul <= n:
    if n % mul == 0:
        multipliers.append(mul)
        n //= mul
    else:
        mul += 1
multipliers.append(n)
print(*multipliers)
