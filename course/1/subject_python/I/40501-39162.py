n_number = int(input())


def checkIsTrueEven(number):
    for digit in str(number):
        if int(digit) % 2 != 0:
            return False
    return True


counter = 0

for number in range(2, n_number + 1, 2):
    if checkIsTrueEven(number):
        counter += 1

print(counter)
