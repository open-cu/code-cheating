n = int(input())
numbers = [int(x) for x in input().split(" ")]


def duolingo(numbers):

    cnt_streak = 0
    streaks = []

    for i in range(len(numbers)):
        if numbers[i] == numbers[i - 1] + 1 or i == 0:
            cnt_streak += 1
        else:
            streaks.append(cnt_streak)
            cnt_streak = 1

    if cnt_streak > 0:
        streaks.append(cnt_streak)

    return len(streaks), streaks


len_streaks, streaks = duolingo(numbers)

print(len_streaks)
print(' '.join(map(str, streaks)))
