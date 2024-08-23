n = int(input())
numbers = [int(x) for x in input().split(" ")]
strike_count = 1
strike_lengths = []
strike_length = 1
i = 1
while i < n:
    if numbers[i] > numbers[i - 1]:
        strike_length += 1
    else:
        strike_lengths.append(strike_length)
        strike_length = 1
        strike_count += 1
    i += 1
strike_lengths.append(strike_length)
print(strike_count)
for num in strike_lengths:
    print(num, end=' ')
