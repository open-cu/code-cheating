n = int(input())
numbers = [int(x) for x in input().split(" ")]
numbers[0] = -abs(numbers[0])
for i in range(1, len(numbers)):
    if -abs(numbers[i]) >= numbers[i - 1]:
        numbers[i] = -abs(numbers[i])
    elif abs(numbers[i]) >= numbers[i - 1]:
        numbers[i] = abs(numbers[i])
    else:
        print('No')
        break
else:
    print('Yes')
    print(*numbers)
