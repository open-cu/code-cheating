import math


def findFirstDelimeter(number):
    for delimeter in range(2, int(math.sqrt(number)) + 1):
        if number % delimeter == 0:
            return delimeter
    return number


def delimetersList(number):
    delimeters = []
    first_delimeter = findFirstDelimeter(number)
    while first_delimeter != number:
        number //= first_delimeter
        delimeters.append(first_delimeter)
        first_delimeter = findFirstDelimeter(number)
    delimeters.append(first_delimeter)
    return delimeters


print(" ".join(list(map(str, delimetersList(int(input()))))))
