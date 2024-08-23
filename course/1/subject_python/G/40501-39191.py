n = int(input())
i = 2
s = []
while i * i <= n:
    while n % i == 0:
        n /= i
        s.append(i)
    i += 1
if n > 1:
    s.append(int(n))
print(' '.join([str(x) for x in s]))
