n = int(input())
numbers = [int(x) for x in input().split(" ")]

strikes_counter = 1
strikes = []

for i in range(1, len(numbers)):
    if numbers[i - 1] < numbers[i]:
        strikes_counter += 1
    else:
        strikes.append(strikes_counter)
        strikes_counter = 1

strikes.append(strikes_counter)
print(len(strikes))
print(*strikes)
