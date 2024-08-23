n = int(input())

nums = list(map(int, input().split()))
res = []
strike_count = 1

for i in range(1, n):

    # начало нового страйка -- значение 1
    if nums[i] == 1:
        # записываем длину прошлого страйка
        res.append(strike_count)
        strike_count = 1
    else:
        strike_count = nums[i]

# записываем длину последнего страйка
res.append(strike_count)

print(len(res))

for i in res:
    print(i, end=' ')
