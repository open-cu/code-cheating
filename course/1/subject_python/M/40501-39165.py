n = int(input())
streaks = [int(i) for i in input().split()]
treaks = []
i = 0
for i in range(len(streaks) - 1):
    if (streaks[i] >= streaks[i + 1]):
        treaks.append(streaks[i])
treaks.append(streaks[-1])
print(len(treaks))
for i in treaks:
    print(i, end=' ')
