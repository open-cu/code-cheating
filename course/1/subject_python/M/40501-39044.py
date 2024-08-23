n = int(input())
nums = list(map(int, input().split()))
res = []
count = 1
for i in range(1, n):
    if nums[i] == 1:
        res.append(count)
        count = 1
    else:
        count = nums[i]
res.append(count)
print(len(res))
for i in res:
    print(i, end=' ')
