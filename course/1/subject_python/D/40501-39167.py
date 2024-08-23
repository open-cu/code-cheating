a = int(input())
b = int(input())
# if the divisor is greater than the denominator, the result of floor division is 0
print(((a * (a // b) + b * (b // a)) // (a // b + b // a)))