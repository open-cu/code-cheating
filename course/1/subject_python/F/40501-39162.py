import math


def countOfDelimeters(number):
    count_of_delimeters = 0
    for delimeter in range(1, int(math.sqrt(number)) + 1):
        if number % delimeter == 0:
            count_of_delimeters += 1

            if delimeter != number // delimeter:
                count_of_delimeters += 1

    return count_of_delimeters


print(countOfDelimeters(int(input())))
