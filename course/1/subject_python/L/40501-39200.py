n = int(input())
numbers = [int(x) for x in input().split(" ")]
if numbers[0] > 0:
    numbers[0] *= -1
i = 1
while i < n:
    if -abs(numbers[i]) >= numbers[i - 1]:
        if numbers[i] > 0:
            numbers[i] *= -1
        i += 1
    elif abs(numbers[i]) >= numbers[i - 1]:
        if numbers[i] < 0:
            numbers[i] *= -1
        i += 1
    else:
        break
if i == n:
    print('Yes')
    print(*numbers)
else:
    print('No')
