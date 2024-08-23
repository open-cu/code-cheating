n = int(input())
lst = list(map(int, input().split()))
flag = True

if lst[0] > 0:
    lst[0] *= -1


for i in range(1, len(lst)):
    if lst[i - 1] <= lst[i] < 0:
        continue
    if lst[i] > 0 and -lst[i] >= lst[i - 1]:
        lst[i] *= -1
    elif -lst[i] >= lst[i - 1]:
        lst[i] *= -1
    elif lst[i] < lst[i - 1]:
        flag = False
        break

if flag:
    print("Yes")
    print(*lst)
else:
    print("No")
