def fibonacci(number: int) -> int:
    if number <= 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(2, number):
            a, b = b, a + b
        return b


test = int(input())
print(fibonacci(test))
