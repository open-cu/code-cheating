def simple(n):
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            print("composite")
            break
    else:
        print("prime")


n = int(input())
simple(n)