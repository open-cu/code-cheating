def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(str(int(i)))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(str(int(n)))
    return primfac


n = int(input())
print(" ".join(primfacs(n)))
