n = int(input())
x = 1
y = 1
for i in range(n - 2):
    tmp = y
    y += x
    x = tmp
print(y)
