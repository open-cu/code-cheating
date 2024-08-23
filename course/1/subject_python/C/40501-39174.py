a = int(input())
b = int(input())

print((a + b - (a % b + b % a) - (a % b + b % a) * (a // b + b // a)) * (b - a) + 1)
