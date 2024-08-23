n = int(input())
streaks = list(map(int, input().split()))
streak_lens = []
for i in range(1, len(streaks)):
    if streaks[i - 1] >= streaks[i]:
        streak_lens.append(streaks[i - 1])
streak_lens.append(streaks[-1])

print(len(streak_lens))
print(*streak_lens)
