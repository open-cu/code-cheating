def isEven(num):
    return num % 2 == 0


def isHonestlyEven(number):
    digits = [int(digit) for digit in str(number)]  # Преобразуем число в список цифр
    return all(isEven(digit) for digit in digits)


def countHonestlyEvenNumbers(n):
    count = 0
    for i in range(1, n + 1):
        if isHonestlyEven(i):
            count += 1
    return count


n = int(input())
print(countHonestlyEvenNumbers(n))
