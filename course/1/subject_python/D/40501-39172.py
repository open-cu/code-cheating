a = int(input())
b = int(input())

ans = (a // b * a + b // a * b) // (b // a + a // b)
print(ans)