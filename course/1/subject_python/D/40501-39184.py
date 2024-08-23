n1 = int(input())
n2 = int(input())
a = n1 // n2
b = n2 // n1
print(((a * n1 + b * n2) // (a + b)))
