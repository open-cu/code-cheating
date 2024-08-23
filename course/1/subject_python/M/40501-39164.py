n = int(input())
numbers = [int(x) for x in input().split(" ")]
k = 0
len_lst = []
length = 0
i = 0
while i < n:
    if numbers[i] == 1:
        k += 1
        length += 1
        if i < n:
            i += 1
            while i != n and numbers[i] != 1:
                length += 1
                i += 1
        len_lst += [length]
        length = 0
print(k)
print(' '.join(map(str, len_lst)))
