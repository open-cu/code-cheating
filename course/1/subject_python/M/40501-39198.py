n = int(input())
nums = [int(x) for x in input().split()]
streaks = []
cur_streak = 0
for x in nums:
    if x == 1 and cur_streak:
        streaks.append(cur_streak)
        cur_streak = 1
    else:
        cur_streak += 1
streaks.append(cur_streak)
print(len(streaks))
print(' '.join([str(x) for x in streaks]))