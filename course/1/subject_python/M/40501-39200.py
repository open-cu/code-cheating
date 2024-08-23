n = int(input())
numbers = [int(x) for x in input().split(" ")]
streak = 1
ans = []
for i in range(1, n):
    if numbers[i] == 1:
        ans.append(streak)
        streak = 1
    else:
        streak += 1
ans.append(streak)
print(len(ans))
print(*ans)
