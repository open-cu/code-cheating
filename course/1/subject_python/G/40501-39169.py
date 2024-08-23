n = int(input())
list_ = []


def deviders(n):
    for i in range(2, int(round(n ** (0.5))) + 1):
        if (n % i) == 0:
            list_.append(i)
            return deviders(n // i)
    list_.append(n)


deviders(n)
list_.sort()
print(" ".join(map(str, list_)))
