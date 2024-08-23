n = int(input())
div = 0
i = 2

while i * i < n + 1:
    if n % i == 0:
        div += 1

    i += 1

if div == 0:
    print("prime")

else:
    print("composite")
