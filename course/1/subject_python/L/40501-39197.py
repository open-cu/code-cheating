n = int(input())
arr = list(map(int, input().split()))
num_p = []
counter_p = 0
counter_n = 0
counter = 0
res = []
flag = True

for i in range(len(arr)):
    num_p.append(abs(arr[i]))

for i in range(len(num_p) - 1):
    if num_p[i] <= num_p[i + 1]:
        counter_p += 1
    elif num_p[i] >= num_p[i + 1]:
        counter_n += 1

i_min = 0

if counter != len(num_p):
    i_min = num_p.index(min(num_p))
    for i in range(i_min - 1):
        if num_p[i] >= num_p[i + 1]:
            counter -= 1
        else:
            flag = False
    for i in range(i_min, len(num_p) - 1):
        if num_p[i] <= num_p[i + 1]:
            counter -= 1
        else:
            flag = False

if counter <= 0 and flag is True:
    for i in range(i_min + 1):
        res.append(num_p[i] * (-1))
    for i in range(i_min + 1, len(num_p)):
        res.append(num_p[i])
    print('Yes')
    print(' '.join(map(str, res)))
elif counter_p == len(num_p):
    print('Yes')
    print(' '.join(map(str, num_p)))
elif counter_n == len(num_p):
    for i in range(len(num_p)):
        num_p[i] = num_p[i] * (-1)
    print('Yes')
    print(' '.join(map((str, num_p))))
else:
    print('No')
