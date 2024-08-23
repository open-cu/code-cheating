def gcd(a, b):
    if a < b:
        tmp = b
        b = a
        a = tmp
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())
numbers = [int(x) for x in input().split(" ")]
if n == 1:
    print(numbers[0])
else:
    num1 = numbers[0]
    num2 = numbers[1]
    num1 = gcd(num1, num2)
    for i in range(2, len(numbers)):
        num2 = numbers[i]
        num1 = gcd(num1, num2)
    print(num1)
