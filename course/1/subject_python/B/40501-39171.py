n = int(input())
a = 1
b = 1
counts = 2
while counts < n:
    a, b = b, a + b
    counts += 1
print(b)
