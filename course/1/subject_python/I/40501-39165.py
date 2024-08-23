def check_true(n):
    while n % 2 == 0:
        n = n // 10
        if n == 0:
            return True
    return False


n = int(input())
count = 0
for i in range(2, n + 1, 2):
    if check_true(i):
        count += 1
print(count)
