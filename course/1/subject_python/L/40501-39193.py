n = int(input())

a = [int(i) for i in input().split()]

index_of_min = 0
for i in range(n):
    if abs(a[i]) <= abs(a[index_of_min]):
        index_of_min = i

flag = 1

for i in range(0, index_of_min):
    cond = abs(a[i]) >= abs(a[i + 1])
    if not cond:
        flag = 0
        break

for i in range(index_of_min, n - 1):
    cond = abs(a[i]) <= abs(a[i + 1])
    if not cond:
        flag = 0
        break

if flag:
    print('Yes')

    for i in range(0, index_of_min):
        if a[i] <= 0:
            print(a[i], end=' ')
        else:
            print(-a[i], end=' ')
    for i in range(index_of_min, n):
        if a[i] >= 0:
            print(a[i], end=' ')
        else:
            print(-a[i], end=' ')
else:
    print('No')
