def lenStrike(lst):
    res = []
    i = 1
    while i < len(lst):
        if lst[i] == lst[i - 1]:
            res.append(1)
            i += 1
        elif lst[i] < lst[i - 1]:
            i += 1
        else:
            count = 1
            while i < len(lst) and lst[i] > lst[i - 1]:
                count += 1
                i += 1
            res.append(count)
    if lst[-1] == 1:
        res.append(1)
    return res


n = int(input())
numbers = [int(x) for x in input().split(" ")]
result = lenStrike(numbers)

print(len(result))
print(*result, sep=' ')
