n = int(input())
array = list(map(int, input().split()))
strikes_length = []
strikes_count = 1
for i in range(1, n):
    if array[i] == 1:
        strikes_count += 1
        strikes_length.append(array[i - 1])
strikes_length.append(array[n - 1])
print(strikes_count)
print(*strikes_length)
