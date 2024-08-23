n = int(input())
i = 2
multipl = []
while i**2 <= n:
    while n % i == 0:
        multipl.append(i)
        n /= i
        n = int(n)
    i += 1
if n > 1:
    multipl.append(n)
print(*multipl, sep=' ')
