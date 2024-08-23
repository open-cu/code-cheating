n = int(input())
arr = list(map(int, input().split()))
res = []

count = 1
for i in range(len(arr)):
    if i + 1 < len(arr) and arr[i] < arr[i + 1]:
        count += 1
    else:
        res.append(count)
        count = 1
print(len(res))
print(*res)
