n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    print(fib[n])