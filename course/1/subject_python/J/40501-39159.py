def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while (b > 0):
        a, b = b, a % b
    return a


def mega_gcd(numbers):
    while (len(numbers) > 1):
        numbers.append(gcd(numbers.pop(), numbers.pop()))
    return numbers[0]


n = int(input())
numbers = [int(x) for x in input().split(" ")]

print(mega_gcd(numbers))
