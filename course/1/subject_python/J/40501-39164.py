def evkl(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


n = int(input())
numbers = [int(x) for x in input().split(" ")]
for i in range(0, n - 1):
    numbers[i + 1] = evkl(numbers[i], numbers[i + 1])
print(numbers[-1])
