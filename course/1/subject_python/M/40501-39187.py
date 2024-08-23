days = int(input())
lineup = list(map(int, input().split()))
strike = []
for i in range(0, len(lineup) - 1):
    if lineup[i] >= lineup[i + 1]:
        strike.append(lineup[i])
strike.append(lineup[days - 1])
print(len(strike), end='\n')
for i in strike:
    print(i, end=' ')