n = int(input())
previus = 1
value = 1
if n <= 2:
    sum_ = 1
else:
    for i in range(1, n - 1):
        sum_ = previus + value
        value = previus
        previus = sum_
print(sum_)
