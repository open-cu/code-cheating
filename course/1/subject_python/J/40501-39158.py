n = int(input())
numbers = [int(x) for x in input().split(" ")]


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def gcd_main(numbers):
    temp = numbers[0]

    for num in numbers[1:]:
        temp = gcd(temp, num)

    return temp


print(gcd_main(numbers))
