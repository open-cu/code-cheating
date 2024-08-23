def count_streaks():
    elements_count = int(input())
    elements = [int(element) for element in input().split()]

    if len(elements) < 2:
        print('1\n1')
        return

    streaks_count = 0
    streak_lengths = []
    current_streak = 1

    for i in range(1, elements_count):
        if elements[i] > elements[i - 1]:
            current_streak += 1
        else:
            streaks_count += 1
            streak_lengths.append(current_streak)
            current_streak = 1

    streak_lengths.append(current_streak)
    streaks_count += 1

    print(streaks_count)
    print(*streak_lengths)


if __name__ == '__main__':
    count_streaks()
