n = int(input())

divisor = 2
while n != 1:
    if divisor > int(n**0.5):
        print(n)
        break

    while n % divisor == 0:
        n //= divisor
        print(divisor, end=' ')

    if divisor > 2:
        divisor += 2
    else:
        divisor += 1
