n = int(input())
if n <= 2:
    print(1)
else:
    fib = [1, 1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    print(fib[-1])
