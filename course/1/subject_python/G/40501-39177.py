mn = []
k = 2
x = int(input())
init = x
while k <= x ** 0.5:
    if x % k == 0:
        x = x / k
        mn.append(str(k))
    else:
        k += 1
mn.append(str(int(x)))
print(' '.join(mn))