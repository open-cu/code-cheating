def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1

    if num1 == 0:
        return num2
    else:
        return num1


n = int(input(''))
lst = list(map(int, input().split(' ')[:n]))
if len(lst) == 1:
    print(lst[0])
else:
    NOD = gcd(lst[0], lst[1])
    for i in range(2, len(lst)):
        NOD = gcd(NOD, lst[i])
    print(NOD)
