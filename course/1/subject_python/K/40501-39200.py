s = input()
ans = ''
cnt = 0
for i in s:
    if i.isalpha() and cnt != 0:
        ans += i * cnt
        cnt = 0
    elif i.isalpha():
        ans += i
    else:
        cnt *= 10
        cnt += int(i)
print(ans)
