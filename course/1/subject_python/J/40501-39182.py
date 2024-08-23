from math import gcd
n = int(input())
numbers = [int(x) for x in input().split(" ")]
maxi = numbers[0]
for i in range(1, n):
    number = numbers[i]
    maxi = gcd(maxi, number)
print(maxi)
