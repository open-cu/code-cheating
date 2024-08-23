n = int(input())
a, b = 1, 1
if n == 2:
    print(a)
else:
    for x in range(3, n + 1):
        a, b = b, a + b
    print(b)
