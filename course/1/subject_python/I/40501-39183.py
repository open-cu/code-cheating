def array_of_dev(n: int) -> int:
    array = []
    x = 1
    while n // x != 0:
        x = x * 10
        array.append(int((n % x - n % (x / 10)) / (x / 10)))
    return array


def calc(n: int) -> int:
    result = 0
    x = 1
    count = 0
    while x <= n:
        check = True
        div_arr = array_of_dev(x)
        for c in range(len(div_arr)):
            if div_arr[c] % 2 != 0:
                check = False
                count = c
        if check:
            result += 1
        x = x - x % (10 ** count) + 10 ** count
        count = 0
    return result


num = int(input())
print(calc(num))
