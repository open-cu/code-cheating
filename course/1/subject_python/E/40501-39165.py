n = int(input())
if n % 2 == 0:
    print("composite" if n != 2 else "prime")
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            print("composite")
            break
    else:
        print("prime")
