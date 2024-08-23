def check_simple(n: int) -> bool:
    for x in range(2, int(n**(0.5)) + 1):
        if n % x == 0:
            return False
    return True


def calc(n: int) -> list:
    result = []
    i = int(n**(0.5)) + 1
    while i > 1:
        if n % i == 0:
            if not check_simple(i):
                result.extend(calc(i))
            else:
                result.append(i)
            n = n // i
            i = int(n**(0.5)) + 1
        else:
            i -= 1

    if n > 1:
        result.append(n)
    return sorted(result)


n = int(input())
print(*calc(n) if not check_simple(n) else [n])
