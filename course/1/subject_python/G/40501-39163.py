n = int(input())
i = 2
res = []
while i**2 <= n:
    while n % i == 0:
        res.append(i)
        n /= i
    i += 1
if n > 1:
    res.append(int(n))
print(*res)