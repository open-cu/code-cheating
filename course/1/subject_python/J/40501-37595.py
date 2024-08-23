n = int(input())

arr = [int(x) for x in input().split()]


def gcd(a, b):
    # Находим НОД двух чисел с помощью Алгоритма Евклида

    r = a % b

    while r:
        a = b
        b = r
        r = a % b

    return b


if len(arr) == 1:
    print(arr[0])

else:
    res = gcd(arr[0], arr[1])

    for i in range(2, len(arr)):

        res = gcd(res, arr[i])

    print(res)
