def check(s):
    flag = True
    for i in range(len(s) // 2):
        flag = flag and (s[i] == s[len(s) - i - 1])
    return flag


s = input()

x = s[0]
count_l = 0
while x == "a":
    count_l += 1
    if count_l == len(s):
        count_l -= 1
        break
    x = s[count_l]

x = s[-1]
count_r = 0
while x == "a":
    count_r += 1
    if count_r == len(s):
        count_r -= 1
        break
    x = s[len(s) - count_r - 1]

if check(s[count_l: len(s) - count_r]) and (count_r >= count_l):
    print("Yes")
else:
    print("No")
