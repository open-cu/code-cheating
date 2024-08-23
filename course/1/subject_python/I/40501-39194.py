n = int(input())
even = 0
for a in range(1, n + 1):
    flag = True
    while a > 0:
        if (a % 10) % 2 != 0:
            flag = False
            break
        else:
            a = a // 10
    if flag:
        even += 1
print(even)
