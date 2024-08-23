n = int(input())
a = 1
b = 1
c = a + b
for i in range(2, n - 1):
    a = c
    c += b
    b = a
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    print(c)
