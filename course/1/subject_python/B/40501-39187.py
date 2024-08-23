n = int(input())
a1 = 1
a2 = 1
a3 = 0
while n > 2:
    n -= 1
    a3 = a2
    a2 += a1
    a1 = a3
print(a2)
