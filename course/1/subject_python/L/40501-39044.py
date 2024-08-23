n = int(input())
res = list(map(int, input().split()))
check = True
if res[0] > 0:
    res[0] = res[0] * (-1)
for i in range(1, n):
    a = res[i]
    b = res[i] * (-1)
    if b >= res[i - 1] and a < res[i - 1]:
        res[i] = b
    elif a >= res[i - 1] and b >= res[i - 1]:
        if b < a:
            res[i] = b
    elif a < res[i - 1] and b < res[i - 1]:
        check = False
if check:
    print("Yes")
    for i in res:
        print(i)
else:
    print("No")
