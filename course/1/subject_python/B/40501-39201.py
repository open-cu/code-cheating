n = int(input())
if n <= 2:
    f = 1
else:
    f_minus_1 = 1
    f_minus_2 = 1
    for i in range(3, n+1):
        f = f_minus_1 + f_minus_2
        f_minus_2 = f_minus_1
        f_minus_1 = f
print(f)