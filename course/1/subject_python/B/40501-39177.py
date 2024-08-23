f1 = 1
f2 = 1

n = int(input()) - 2
 
for _ in range(n):
    f1, f2 = f2, f1 + f2
print(f2)