def duolingo(numbers: list) -> list:
    strike_count = 0
    strikes = []
    for number in numbers:
        if number > strike_count:
            strike_count = number
        else:
            strikes.append(strike_count)
            strike_count = 1
    strikes.append(strike_count)
    return strikes


n_test = int(input())
numbers_test = [int(x) for x in input().split(" ")]

print(len(duolingo(numbers_test)))
print(*duolingo(numbers_test))
