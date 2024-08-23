n = int(input())
a = 2
while a**2 <= n and n % a != 0:
    a += 1
if a**2 > n:
    print("prime")
else:
    print("composite")
