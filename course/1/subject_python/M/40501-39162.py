_ = input()
array = list(map(int, input().split()))

strikes = []
current_strike = 1

for i in range(len(array) - 1):
    if array[i] < array[i + 1]:
        current_strike += 1
    else:
        strikes.append(current_strike)
        current_strike = 1
strikes.append(current_strike)

print(len(strikes))
print(*strikes)
