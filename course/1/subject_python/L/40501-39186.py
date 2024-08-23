def is_non_decreasing(n, arr):
    if n == 1:
        res = True
    else:
        i = 1
        while i < n and abs(arr[i - 1]) >= abs(arr[i]):
            if arr[i - 1] > 0:
                arr[i - 1] = - arr[i - 1]
            i += 1
        while i < n and abs(arr[i - 1]) <= abs(arr[i]):
            if arr[i - 1] < 0:
                arr[i - 1] = - arr[i - 1]
            if arr[i] < 0:
                arr[i] = - arr[i]
            i += 1
        res = True if i % n == 0 else False
    return res


n = int(input())
numbers = [int(x) for x in input().split(" ")]

if is_non_decreasing(n, numbers):
    print("Yes")
    print(*numbers, sep=' ')
else:
    print("No")
