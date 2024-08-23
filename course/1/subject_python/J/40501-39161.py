n = int(input())
numbers = [int(x) for x in input().split(" ")]


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


common_gcd = numbers[0]

for i in range(1, len(numbers)):
    common_gcd = gcd(common_gcd, numbers[i])

print(common_gcd)
