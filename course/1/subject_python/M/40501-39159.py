n = int(input())
numbers = [int(x) for x in input().split(" ")]

count_of_strikes = 0
len_of_strikes = []
for i in range(n):
    if (numbers[i] == 1):
        count_of_strikes += 1
        if (i > 0):
            len_of_strikes.append(numbers[i - 1])
len_of_strikes.append(numbers[-1])

print(count_of_strikes)
for length in len_of_strikes:
    print(length, end=' ')
