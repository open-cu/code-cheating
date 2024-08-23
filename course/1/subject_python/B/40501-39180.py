n = int(input())

s1, s2 = 1, 1

for i in range(2, n):
    s1, s2 = s2, s1+s2
print(s2)