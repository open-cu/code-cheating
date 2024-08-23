n = int(input())
a = 1
b = 1
for i in range(n - 2):
    temp = b
    b = a + b
    a = temp
print(b)