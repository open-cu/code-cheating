n = int(input())
honest_even_count = 0
for number in range(2, n + 1):
    if all(digit % 2 == 0 for digit in map(int, str(number))):
        honest_even_count += 1
print(honest_even_count)
