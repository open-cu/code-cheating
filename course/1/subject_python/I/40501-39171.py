n = int(input())
count = 0
for i in range(1, n + 1):
    is_fair_even = True
    for digit in str(i):
        if int(digit) % 2 != 0:
            is_fair_even = False
            break
    if is_fair_even:
        count += 1
print(count)
