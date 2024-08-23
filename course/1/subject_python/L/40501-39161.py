n = int(input())
numbers = [int(x) for x in input().split(" ")]

numbers[0] = min(numbers[0], -numbers[0])

for idx in range(1, len(numbers)):
    min_number = min(numbers[idx], -numbers[idx])

    if min_number >= numbers[idx - 1]:
        numbers[idx] = min_number
    else:
        numbers[idx] = -min_number

    if numbers[idx - 1] > numbers[idx]:
        print('No')
        break
else:
    print('Yes')
    print(*numbers)
