a = int(input())
b = int(input())
answer = ((a + b) * (a // b + b // a) + a % b + b % a - a - b) // (a // b + b // a)
print(answer)
