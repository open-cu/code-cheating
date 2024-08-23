count = int(input())
numbers = [int(x) for x in input().split(" ")]


def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


a = numbers[0]
i = 1
while i < len(numbers):
    a = gcd_rem_division(numbers[i], a)
    i += 1

print(a)
