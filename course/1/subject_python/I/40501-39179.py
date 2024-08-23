n = int(input())
temp = 0  # Порядок числа
res = 0
i = 2
flag = True
while i <= n:
    flag = True
    for let in str(i):
        if int(let) % 2 == 1:
            flag = False
    if flag:
        res += 1
        i += 2
    else:
        for j in range(len(str(i)), -1, -1):
            if int(j) % 2 == 0:
                temp += 1
            else:
                i += 10 ** temp
                break
        temp = 0

print(res)
