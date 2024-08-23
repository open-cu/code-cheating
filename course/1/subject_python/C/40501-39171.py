a = int(input())
b = int(input())
is_divisible = 1 - ((a % b) * (b % a))
print(is_divisible)
