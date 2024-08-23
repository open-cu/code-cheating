def find_NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def many_NOD(n, arr):
    if len(arr) == 1:
        return arr[0]
    else:
        NOD = find_NOD(arr[0], arr[1])
        for i in range(1, n):
            NOD = find_NOD(NOD, arr[i])
    return NOD


n = int(input())
arr = list(map(int, input().split()))
print(many_NOD(n, arr))
