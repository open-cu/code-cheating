fibonacciNum = int(input())

if fibonacciNum <= 2:
    print(1)
else:
    prevFibonacci = 1
    curFibonacci = 1

    for i in range(fibonacciNum - 2):
        curFibonacci += prevFibonacci
        prevFibonacci = curFibonacci - prevFibonacci

    print(curFibonacci)
