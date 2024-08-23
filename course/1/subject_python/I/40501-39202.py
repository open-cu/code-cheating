def right_odd(n):
    digit = []

    while (n > 0):
        digit.append(n % 10)
        n = n // 10

    for i in range(len(digit)):
        if digit[i] % 2 == 1:
            return 0
    return 1


num = int(input(''))
cnt = 0


for i in range(1, num + 1):
    if right_odd(i) == 1:
        cnt += 1
print(cnt)
