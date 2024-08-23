n = int(input())
prime = True
i = 2
while i <= n ** 0.5 and prime is True:
    if n % i == 0:
        prime = False
    i += 1
if prime:
    print("prime")
else:
    print("composite")
