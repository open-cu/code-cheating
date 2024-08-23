n = int(input())

a = 1
b = 1
for i in range(n - 2):
    c = b
    b = b + a
    a = c
print(b)
