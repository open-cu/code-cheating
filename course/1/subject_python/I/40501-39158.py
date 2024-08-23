n = int(input())


def is_even(n):
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 != 0:
            return False
        n //= 10
    return True


def count_even_numbers(n):
    cnt = 0
    for i in range(1, n + 1):
        if is_even(i):
            cnt += 1
    return cnt


print(count_even_numbers(n))
