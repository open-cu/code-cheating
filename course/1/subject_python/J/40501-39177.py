def GCD(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a + b


n = int(input())
s = list(map(int, input().split(" ")))
a = s[0]
for b in s[1:]:
    a = GCD(b, a)

print(a)
