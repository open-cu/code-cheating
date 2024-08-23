n = int(input())

if n > 2:
    a, b = 1, 1
    for i in range(n - 2):
        a, b = a + b, a
    print(a)
else:
    print(1)
