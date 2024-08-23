def gcd_of_two_nums(a, b):
    # a = bq + r
    # (a,b) = (b, r) .. = (k, 0) = k
    if a < b:
        a, b = b, a

    while b > 0:
        r = a % b
        a, b = b, r

    return a


def gcd(*args):
    if len(args) == 1:
        return args[0]
    # (a,b,c) = ((a,b), c)
    ans = gcd_of_two_nums(args[0], args[1])

    for i in range(2, len(args)):
        ans = gcd_of_two_nums(ans, args[i])

    return ans


n = int(input())
nums = map(int, input().split(" "))
print(gcd(*nums))
