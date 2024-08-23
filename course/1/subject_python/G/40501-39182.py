number = int(input())
while number % 2 == 0:
    print(2, end=' ')
    number //= 2

i = 3
while i * i <= number:
    while number % i == 0:
        print(i, end=' ')
        number //= i
    i += 2

if number > 2:
    print(number)
