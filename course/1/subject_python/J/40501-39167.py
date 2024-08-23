def count_gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % a
    return abs(a)


n = int(input())
nums = list(map(int, input().split()))
NOD = nums[0]
for i in range(1, n):
    NOD = count_gcd(NOD, nums[i])
print(NOD)
