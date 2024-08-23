n = int(input())
s = [int(x) for x in input().split()]
s.append(1)
k = 0
size = 1
a = []
for i in range(1, n + 1):
    if s[i] > s[i - 1]:
        size += 1
    else:
        k += 1
        a.append(size)
        size = 1
print(k)
for i in range(0, k):
    print(a[i], end=' ')
