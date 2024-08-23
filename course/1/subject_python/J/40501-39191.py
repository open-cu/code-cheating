import math
n = int(input())
numbers = list(map(int, input().split()))
result = numbers[0]
for i in range(1, n):
    result = math.gcd(result, numbers[i])
print(result)
