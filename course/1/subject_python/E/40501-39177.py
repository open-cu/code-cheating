x = int(input())
flag = 0
if x % 2 == 0 and x != 2:
    flag = 1
else:
    n = x ** 0.5 // 1
    for i in range(3, int(n + 1), 2):
        if x % i == 0:
            flag = 1
            break
print('composite') if flag == 1 else print('prime')