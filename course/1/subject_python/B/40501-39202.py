def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


num = int(input(''))

if (num == 1) or (num == 2):
    print('1')
else:
    print(fib(num))
