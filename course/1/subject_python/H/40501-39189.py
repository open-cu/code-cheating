inp = input()

left_a_cnt = 0
right_a_cnt = 0

for i in range(len(inp)):
    if inp[i] != 'a':
        break
    else:
        left_a_cnt += 1

for i in range(len(inp) - 1, -1, -1):
    if inp[i] != 'a':
        break
    else:
        right_a_cnt += 1

if left_a_cnt == len(inp):
    print("Yes")
elif left_a_cnt > right_a_cnt:
    print("No")
else:
    for i in range((len(inp) - left_a_cnt - right_a_cnt) // 2):
        if inp[left_a_cnt + i] != inp[len(inp) - right_a_cnt - i - 1]:
            print("No")
            break
    else:
        print("Yes")
