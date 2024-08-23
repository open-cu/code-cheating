n = int(input())

f = [1, 1]

for i in range(2, n):

    fi = f[-1] + f[-2]
    f.append(fi)

print(f[-1])
