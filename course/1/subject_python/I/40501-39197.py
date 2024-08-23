n = int(input())
res = 0
for i in range(0, n + 1, 2):
    count = 0
    for k in str(i):
        if k in '02468':
            count += 1
    if count == len(str(i)):
        res += 1
print(res - 1)
