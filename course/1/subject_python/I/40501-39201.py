def is_even_digits(number):
    while number > 0:
        digit = number % 10
        if digit % 2 != 0:
            return False
        number //= 10
    return True


n = int(input())
counter = 0
number = 2

while number <= n:
    if is_even_digits(number):
        counter += 1
    number += 2

print(counter)
