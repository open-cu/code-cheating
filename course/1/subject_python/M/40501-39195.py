def strike_count(arr):
    count = 0
    res = []

    for i, n in enumerate(arr):
        if n == 1:
            count += 1
            if i > 0:
                res.append(arr[i - 1])

    if count > 0:
        res.append(arr[-1])

    print(count)
    print(*res)


def solution():
    input()
    arr = [int(i) for i in input().split()]
    strike_count(arr)


solution()
