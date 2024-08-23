n = int(input())
arr = list(map(int, input().split(" ")))
if arr[0] > 0:
    arr[0] *= -1
i = 1
while i < n:
    if - abs(arr[i]) >= arr[i - 1]:
        if arr[i] > 0:
            arr[i] *= -1
        i += 1
    elif abs(arr[i]) >= arr[i - 1]:
        if arr[i] < 0:
            arr[i] *= -1
        i += 1
    else:
        break
if i == n:
    print('Yes')
    print(*arr)
else:
    print('No')
