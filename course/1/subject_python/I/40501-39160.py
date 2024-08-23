n = int(input())


def checker(n):
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 == 0:
            n = n // 10
        else:
            return False

    return True


answer = 0

for i in range(1, n + 1):
    answer += checker(i)

print(answer)
