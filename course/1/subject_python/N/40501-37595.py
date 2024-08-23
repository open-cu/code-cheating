round_str = input()
target_str = input()

len_round = len(round_str)
len_target = len(target_str)

flag = False

for i in range(len_round):
    candidate = ''
    for j in range(len_target):
        candidate += round_str[(i + j) % len_round]
    if (candidate == target_str):
        flag = True

target_str = target_str[::-1]

for i in range(len_round):
    candidate = ''
    for j in range(len_target):
        candidate += round_str[(i + j) % len_round]
    if (candidate == target_str):
        flag = True

if not flag:
    print('NO')
else:
    print('YES')
