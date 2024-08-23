n = int(input())
numbers = [int(x) for x in input().split(" ")]

increase = -1
decrease = -1
for i in range(1, n):
    if (abs(numbers[i]) - abs(numbers[i - 1]) > 0):
        increase = i
    if (abs(numbers[i]) - abs(numbers[i - 1]) < 0):
        if (increase > 0):
            print('No')
            break
        else:
            decrease = i
else:
    print('Yes')
    for i in range(decrease + 1):
        print(- abs(numbers[i]), end=' ')
    for i in range(decrease + 1, n):
        print(abs(numbers[i]), end=' ')
