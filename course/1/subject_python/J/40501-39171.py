n = int(input())
numbers = [int(x) for x in input().split(" ")]
gcd = numbers[0]
for num in numbers[1:]:
    while num != 0:
        gcd, num = num, gcd % num
print(gcd)
