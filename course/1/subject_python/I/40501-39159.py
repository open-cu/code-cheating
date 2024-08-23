n = int(input())

count = 0
for i in range(2, n + 1, 2):
    while (i > 0):
        if ((i % 10) % 2 != 0):
            break
        i = i // 10
    else:
        count += 1

print(count)
