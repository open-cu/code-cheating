def is_even_digit(num):
    while num > 0:
        digit = num % 10
        if digit % 2 != 0:
            return False
        num //= 10
    return True


def count_honestly_even_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if is_even_digit(i):
            count += 1
    return count


n = int(input())

result = count_honestly_even_numbers(n)
print(result)
