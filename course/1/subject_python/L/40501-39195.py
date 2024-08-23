def non_decr(arr):
    for i in range(len(arr)):
        if i == 0:
            if arr[i] > 0:
                arr[i] *= -1
        else:
            if arr[i] > 0 and -arr[i] >= arr[i - 1]:
                arr[i] *= -1
            elif arr[i] < 0 and arr[i] < arr[i - 1]:
                arr[i] *= -1

        if i > 0 and arr[i] < arr[i - 1]:
            print("No")
            return

    print("Yes")
    print(*arr)


def solution():
    input()
    arr = [int(i) for i in input().split()]

    non_decr(arr)


solution()
