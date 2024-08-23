def main(arr):
    if -arr[0] < arr[0]:
        arr[0] = -arr[0]

    flag = True

    for i in range(1, n):
        # print(arr[i - 1], arr[i])
        if arr[i] >= arr[i - 1]:
            if arr[i] >= -arr[i] >= arr[i - 1]:
                arr[i] = -arr[i]
        else:
            if -arr[i] >= arr[i - 1]:
                arr[i] = -arr[i]
            else:
                flag = False
                return flag, []
        # print(arr)
    return flag, arr


n = int(input())
arr = list(map(int, input().split()))

flag, arr = main(arr)

if not flag:
    print("No")
else:
    print("Yes")
    print(" ".join([str(el) for el in arr]))
