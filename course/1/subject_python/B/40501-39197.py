# ex_1
# t = input()
# if 'a' <= t[0] <= 'z' and '0' <= t[1] <= '9' or 'a' <= t[1] <= 'z' and '0' <= t[0] <= '9':
#     print('YES')
# else:
#     print('NO')

# ex_2

n = int(input())
f_1 = 1
f_2 = 1
i = 2
while i < n:
    f_2, f_1 = f_2 + f_1, f_2
    i += 1
print(f_2)