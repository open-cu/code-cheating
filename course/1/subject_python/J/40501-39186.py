def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


n = int(input())
numbers = [int(x) for x in input().split(" ")]

res = numbers[n - 1]
while n - 1 > 0:
    res = nod(res, numbers[n - 2])
    n -= 1
print(res)
