n = int(input())
prev = 1
f = 1
buf = 0
for i in range(3, n+1):
    buf = f
    f = f + prev
    prev = buf
print(f)