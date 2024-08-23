n = int(input())
numbers = [int(x) for x in input().split(" ")]
counter = 1

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] != 1:
        counter += 1
print(counter)

straiki = []
counter_straik = 1
for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] == 1:
        counter_straik += 1
        continue
    straiki.append(counter_straik)
    counter_straik = 1
straiki.append(counter_straik)
print(' '.join(map(str, straiki)))
