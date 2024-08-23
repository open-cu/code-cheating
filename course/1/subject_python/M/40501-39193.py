# ввод
n = int(input())
numbers = [int(x) for x in input().split(" ")]

strike_counter = 0
lens_of_strikes = []
previous = None

for i in range(n):
    if numbers[i] == 1:
        strike_counter += 1
        if i != 0:
            lens_of_strikes.append(previous)

    previous = numbers[i]

lens_of_strikes.append(numbers[n - 1])

print(len(lens_of_strikes))

for i in lens_of_strikes:
    print(i, end=' ')
