a = int(input())
b = int(input())
x = ((a // b + 2) // (a // b + 1)) % 2
y = (x + 1) % 2
v = a * x + b * y
print(v)
