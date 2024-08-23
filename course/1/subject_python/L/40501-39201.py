n = int(input())
numbers = [int(x) for x in input().split(" ")]
answer = 'Yes'

if n == 1 or len(set(numbers)) == 1:
    print(answer, ' '.join(map(str, numbers)), sep='\n')

else:
    numbers_old = numbers.copy()
    numbers[0] = - abs(numbers[0])

    for i in range(n - 1):
        a = numbers[i]
        b = numbers[i + 1]

        if a > b and a > -b:
            answer = 'No'
            break
        elif a <= - abs(b):
            numbers[i + 1] = - abs(b)
        elif a > b and a <= -b:
            numbers[i + 1] = - b

    for i in range(n - 2, 1, -1):
        numbers[i] = numbers_old[i] if numbers_old[i] >= numbers[i - 1] and numbers_old[i] <= numbers[i + 1] else -numbers_old[i]

    numbers[0] = numbers_old[0] if numbers_old[0] <= numbers[1] else numbers[0]
    numbers[n - 1] = numbers_old[n - 1] if numbers_old[n - 1] >= numbers[n - 2] else numbers[n - 1]

    print(answer, ' '.join(map(str, numbers)) + ' ' if answer == 'Yes' else '', sep='\n')
