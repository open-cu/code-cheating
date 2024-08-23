a = int(input())
b = int(input())
# print(a // b, b // a, a // b // 1)
res_2 = a // b + b // a
ans = (a + b) / 2 + ((a - b) ** 2) ** 0.5 / 2
# print(res_2)
print(int(ans))
