def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
numbers = [int(x) for x in input().split(" ")]

for i in range(len(numbers) - 1):
    numbers[i + 1] = gcd(numbers[i], numbers[i + 1])

print(numbers[-1])
