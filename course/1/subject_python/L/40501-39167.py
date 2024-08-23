n = int(input())
arr = list(map(int, input().split()))
arr_abs = list(map(abs, arr))
i = 1
while i < n and arr_abs[i] <= arr_abs[i - 1]:
    if arr[i - 1] < 0:
        arr_abs[i - 1] = arr[i - 1]
    else:
        arr_abs[i - 1] *= -1
    i += 1
arr_abs[i - 1] = arr[i - 1]
for k in range(i, n - 1):
    if arr_abs[k] > arr_abs[k + 1]:
        print('No')
        break
else:
    print('Yes')
    print(*arr_abs, sep=' ')
