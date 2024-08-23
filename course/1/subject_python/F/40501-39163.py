n = int(input())
res = 1
a = 2
b = 1
while a**2 <= n:
    d = 1
    while n % a == 0:
        d += 1
        n //= a
    res *= d
    a, b = a + b, 2
if n > 1:
    res *= 2
print(res)
