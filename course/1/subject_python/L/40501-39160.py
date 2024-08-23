n = int(input())
a = list(map(int, input().split()))

flag = False

a[0] = -abs(a[0])

for i in range(1, n):
    if a[i] >= a[i - 1]:
        if -a[i] >= a[i - 1] and -a[i] < a[i]:
            a[i] = -a[i]
    elif -a[i] >= a[i - 1]:
        a[i] = -a[i]
    else:
        flag = True
        break

if not flag:
    print('Yes')
    print(*a)
else:
    print('No')
