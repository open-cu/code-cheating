n1 = int(input())
n2 = int(input())
res = n1 * (1 % (n1 // n2 + 1)) + n2 * (1 % (n2 // (n1 + 1) + 1))
print(res)
