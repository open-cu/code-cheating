a = int(input())
b = int(input())
# res = a % b
res_2 = b // a * (b - b // a * a + 1) - b // a + a // b * (a - a // b * b + 1) - a // b + 1
# print(f'res = {res}\nb // a = {b // a}\nres_2 = {res_2}')
print(res_2)