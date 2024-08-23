n = int(input())
a = input().split(" ")
a = [int(x) for x in a]
list_ = []
k = 1
for i in range(1, len(a)):
    if a[i] <= a[i - 1]:
        list_.append(int(a[i - 1]))
        k += 1
list_.append(int(a[len(a) - 1]))
print(k)
print(" ".join(map(str, list_)))
