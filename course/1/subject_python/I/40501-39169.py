k = 0
n = int(input())
sum_ = 0
for i in range(1, n + 1):
    word = list(str(i))
    for simv in word:
        if int(simv) % 2 == 0:
            k += 1
    if k == len(word):
        sum_ += 1
    k = 0
print(sum_)
