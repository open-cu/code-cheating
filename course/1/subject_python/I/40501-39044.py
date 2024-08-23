n = int(input())
count = 0
for i in range(1, n + 1):
    temp = i
    check = True
    while temp != 0 and check:
        if temp % 10 % 2 == 1:
            check = False
        temp = temp // 10
    if check:
        count = count + 1
print(count)
