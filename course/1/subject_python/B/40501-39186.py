def fibonacci(n):
    fib1 = fib2 = 1
    n = n - 2
    while n > 0:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        n -= 1
    return fib2


n = int(input())
print(fibonacci(n))
