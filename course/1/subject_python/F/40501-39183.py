def calc(n: int) -> int:
    num = 1
    if n > 1:
        num += 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i != int(n**0.5):
                num += 2
            else:
                num += 1
    return num


n = int(input())
print(calc(n))
