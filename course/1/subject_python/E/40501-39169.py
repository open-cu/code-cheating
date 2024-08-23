n = int(input())
sum_ = 0
if n == 2:
    print("prime")
else:
    if n % 2 == 0:
        sum_ = 1
        print("composite")
    else:
        for i in range(3, int(n ** (0.5)) + 1, 2):
            if n % i == 0:
                sum_ = 1
                print("composite")
                break
    if sum_ == 0:
        print("prime")
