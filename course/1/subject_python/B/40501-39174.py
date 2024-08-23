n = int(input())
a1 = 1
a2 = 1
if n == 1 or n == 2:
    print(1)
else:
    for i in range(2, n):
        a1, a2 = a2, a1 + a2
    print(a2)
