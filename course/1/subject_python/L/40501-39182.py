n = int(input())
numbers = list(int(x) for x in input().split(" "))
numbers_positive = []
counter_positive = 0
counter_negative = 0
counter = 0
result = []
flag = True

for i in range(len(numbers)):
    numbers_positive.append(abs(numbers[i]))

for i in range(len(numbers_positive) - 1):
    if numbers_positive[i] <= numbers_positive[i + 1]:
        counter_positive += 1
    elif numbers_positive[i] >= numbers_positive[i + 1]:
        counter_negative += 1

index_min = 0

if counter != len(numbers_positive):
    index_min = numbers_positive.index(min(numbers_positive))
    for i in range(index_min - 1):
        if numbers_positive[i] >= numbers_positive[i + 1]:
            counter -= 1
        else:
            flag = False
    for i in range(index_min, len(numbers_positive) - 1):
        if numbers_positive[i] <= numbers_positive[i + 1]:
            counter -= 1
        else:
            flag = False

if counter <= 0 and flag is True:
    for i in range(index_min + 1):
        result.append(numbers_positive[i] * (-1))
    for i in range(index_min + 1, len(numbers_positive)):
        result.append(numbers_positive[i])
    print('Yes')
    print(' '.join(map(str, result)))
elif counter_positive == len(numbers_positive):
    print('Yes')
    print(' '.join(map(str, numbers_positive)))
elif counter_negative == len(numbers_positive):
    for i in range(len(numbers_positive)):
        numbers_positive[i] = numbers_positive[i] * (-1)
    print('Yes')
    print(' '.join(map((str, numbers_positive))))
else:
    print('No')
