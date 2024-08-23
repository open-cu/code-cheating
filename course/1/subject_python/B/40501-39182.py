f1 = 1
f2 = 1
result = 0
i = 0
n = int(input())
while i < n - 2:
    result = f1 + f2
    f1 = f2
    f2 = result
    i = i + 1
print(f2)
