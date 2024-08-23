n = int(input())
numbers = [int(x) for x in input().split(" ")]

if n == 1:
    print(1, 1, sep='\n')

else:
    counter = 1
    strikes = []
    for i in range(n - 1):
        if numbers[i + 1] == 1:
            counter += 1
            strikes.append(numbers[i])
    strikes.append(numbers[n - 1])

print(counter, ' '.join(map(str, strikes)), sep='\n')
