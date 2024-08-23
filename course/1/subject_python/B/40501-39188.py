n = int(input())

c, p = 0, 1

for _ in range(n):

    c, p = c + p, c

print(c)
