n = int(input())


def checker(n):
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 == 0:
            n = n // 10
        else:
            return False

    return True


x = 1
answer = 0

while x <= n:
    answer += checker(x)
    x += 1

print(answer)
