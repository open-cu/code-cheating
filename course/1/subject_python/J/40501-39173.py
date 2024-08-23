def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


numbers = int(input())
numbers_list = list(map(int, input().split()))
if numbers == 1:
    print(numbers_list[0])
else:
    stored_gcd = euclid(numbers_list[0], numbers_list[1])
    for i in range(1, numbers - 1):
        stored_gcd = euclid(stored_gcd, numbers_list[i + 1])
    print(stored_gcd)
