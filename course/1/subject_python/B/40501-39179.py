def fibonacci(n):
    a = 1
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


n = int(input())
print(fibonacci(n))