def trueev(x):
    for el in str(x):
        if int(el) % 2 == 1:
            return False
    return True


n = int(input())
k = 0
for i in range(1, n + 1):
    if trueev(i):
        k += 1
print(k)
