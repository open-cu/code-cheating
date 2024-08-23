def calc(n: int, arr: list) -> int:
    minimum_div = min(arr)
    while True:
        const = True
        for x in arr:
            if x % minimum_div != 0:
                const = False
        if const:
            break
        minimum_div -= 1
    return minimum_div


n, arr = int(input()), list(map(int, input().split()))
print(calc(n, arr))
