n = int(input())
f1, f2 = 1, 1
for _ in range(n - 2):
    f1, f2 = f1 + f2, f1
print(f1)
