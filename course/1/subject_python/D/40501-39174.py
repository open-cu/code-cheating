a = int(input())
b = int(input())

ans = (a // b * b + b // a * a + (a % b * (a // b) + b % a * (b // a)) // ((b // a) + (a // b))) // (
    (a // b) * (b // a) + 1)

print(ans)