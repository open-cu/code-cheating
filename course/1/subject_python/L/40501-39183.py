def non_decrease(n: int, a: list) -> tuple:
    if a[0] > -a[0]:
        a[0] = -a[0]
    for x in range(1, n):
        if a[x] >= a[x - 1]:
            if -a[x] >= a[x - 1] and -a[x] < a[x]:
                a[x] = -a[x]
        elif -a[x] >= a[x - 1]:
            a[x] = -a[x]
        else:
            return 'No', []
    return 'Yes', a


n, x = int(input()), list(map(int, input().split()))
result = non_decrease(n, x)
print(result[0])
print(*result[1])
