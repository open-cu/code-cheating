n = int(input())

for divider in range(2, int(n ** (1 / 2)) + 1):
    if n % divider == 0:
        print("composite")
        break
else:
    print("prime")
