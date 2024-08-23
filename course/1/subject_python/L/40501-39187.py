n = int(input())
arr = list(map(int, input().split()))
flag = True
if arr[0] > 0:
    arr[0] = -arr[0]
for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        if arr[i] > 0 and -arr[i] >= arr[i - 1]:
            arr[i] = -arr[i]
    elif abs(arr[i]) >= abs(arr[i-1]):
        arr[i] = -arr[i]

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        flag = False
if flag:
    print('Yes')
    for i in arr:
        print(i, end=' ')
else:
    print('No')