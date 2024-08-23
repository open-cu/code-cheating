import math
n = int(input(''))
lst = list(map(int, input().split(' ')[:n]))
lst[0] = int(-math.fabs(lst[0]))
for i in range(1, len(lst)):
    if int(-math.fabs(lst[i])) >= lst[i - 1]:
        lst[i] = int(-math.fabs(lst[i]))
    elif int(math.fabs(lst[i])) >= lst[i - 1]:
        lst[i] = int(math.fabs(lst[i]))
    else:
        print('No')
        break
else:
    print('Yes')
    print(' '.join(map(str, lst)))
        