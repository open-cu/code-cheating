n1 = int(input())
n2 = int(input())
ans = 1 + (n1 % n2) * (n2 % n1)
print(ans)