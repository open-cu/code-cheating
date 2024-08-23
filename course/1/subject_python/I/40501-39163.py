n = int(input())
s = 0
for i in range(0, n+1, 2):
    if all(int(a) % 2 == 0 for a in str(i)):
        s += 1
print(s-1)