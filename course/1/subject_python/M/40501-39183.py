def calc(n: int, x: list) -> list:
    strike = []
    count = 1
    for c in range(n - 1):
        if x[c + 1] > x[c]:
            count += 1
        else:
            strike.append(count)
            count = 1
        if c == n - 2:
            strike.append(count)
    return strike


n, arr = int(input()), list(map(int, input().split()))
arr = list(filter(lambda x: x > 0, calc(n, arr)))
print(len(arr))
print(*arr)
