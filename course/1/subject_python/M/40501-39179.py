n = int(input())
lst = list(map(int, input().split()))

strikes = 0
dur = 1
duration = []

for i in range(len(lst)):
    if lst[i] == 1:
        duration.append(dur)
        dur = 1
        strikes += 1
    else:
        dur += 1

duration.append(dur)
print(strikes)
print(*duration[1:])
