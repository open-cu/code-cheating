def find_strikes_lens(visits):
    if len(visits) == 1:
        return [1]

    strikes_lens = []
    strike_start = 0

    for i in range(1, len(visits)):
        if visits[i] <= visits[i - 1]:
            strikes_lens.append(i - strike_start)
            strike_start = i

        if i == len(visits) - 1:
            if visits[i] <= visits[i - 1]:
                strikes_lens.append(1)
            else:
                strikes_lens.append(i + 1 - strike_start)

    return strikes_lens


_ = input()
visits = list(map(int, input().split()))
strikes_lens = find_strikes_lens(visits)
print(len(strikes_lens))
print(*strikes_lens)
