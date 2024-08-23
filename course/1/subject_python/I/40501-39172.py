def check(x):
    s = str(x)
    flag = True
    for el in s:
        flag = flag and (int(el) % 2 == 0)
    return flag


n = int(input())

count = 0
for i in range(1, n + 1):
    count += check(i)

print(count)
