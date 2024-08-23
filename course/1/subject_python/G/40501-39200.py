def PrimeDivisors(x):
    ans = []
    divisor = 2
    while x >= divisor * divisor:
        while x % divisor == 0:
            ans.append(divisor)
            x = x // divisor
        divisor = divisor + 1
    if x > 1:
        ans.append(x)
    return ans


n = int(input())
print(*PrimeDivisors(n))
