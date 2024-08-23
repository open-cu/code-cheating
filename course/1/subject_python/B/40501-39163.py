n = int(input())
k = 0
f_1 = 1
f_2 = 1
if n == 1 or n == 2:
    print(1)
else:
    for i in range(3, n):
        f_1, f_2 = f_1 + f_2, f_1
    print(f_1 + f_2)
