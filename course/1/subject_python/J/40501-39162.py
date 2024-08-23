def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


n_number = input()
numbers = list(map(int, input().split()))
if len(numbers) == 1:
    print(numbers[0])
else:
    total_gcd = gcd(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        total_gcd = gcd(total_gcd, numbers[i])
    print(total_gcd)
