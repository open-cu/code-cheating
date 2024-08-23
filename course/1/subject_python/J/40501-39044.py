n = int(input())
s = input()
ind = 0
a = list(map(int, s.split()))
c = a[0]
if n == 1:
    print(a[0])
else:
    for i in range(1, n):
        b = a[i]
        while c != 0 and b != 0:
            if c > b:
                c = c % b
            else:
                b = b % c

        c = c + b
    print(c)
