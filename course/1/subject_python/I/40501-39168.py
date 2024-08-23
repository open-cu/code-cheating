n = int(input())

num_true_ = 0

for i in range(1, n + 1):
    iter_i = list(str(i))
    iter_i = [int(j) for j in iter_i]
    p = 0
    for k in iter_i:
        if k % 2 == 1:
            break
        else:
            p += 1
    if p == len(iter_i):
        num_true_ += 1

print(num_true_)
