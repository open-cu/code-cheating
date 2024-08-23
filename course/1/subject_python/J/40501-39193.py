def stealed_gcd(a, b):

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


n = int(input())
numbers = [int(x) for x in input().split(" ")]

mega_gcd = numbers[0]

for i in numbers:
    if mega_gcd == 1:
        break
    mega_gcd = stealed_gcd(mega_gcd, i)

print(mega_gcd)
