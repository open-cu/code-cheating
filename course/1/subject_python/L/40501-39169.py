n = int(input())
a = input().split(" ")
a = [int(x) for x in a]
list_ = []
if int(a[0]) > 0:
    a[0] = a[0] * (-1)
    list_.append(int(a[0]))
else:
    list_.append(int(a[0]))
for i in range(1, len(a)):
    if int(a[i]) * (-1) >= a[i - 1] and a[i] > 0:
        a[i] = int(a[i]) * (-1)
        list_.append(int(a[i]))
    elif int(a[i]) < int(a[i - 1]) and int(a[i]) * (-1) >= int(a[i - 1]):
        a[i] = int(a[i]) * (-1)
        list_.append(int(a[i]))
    elif int(a[i]) >= int(a[i - 1]):
        list_.append(int(a[i]))
if len(list_) == len(a):
    print("Yes")
    print(" ".join(map(str, list_)))
else:
    print("No")
