def mega_nod(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
numbers = list(map(int, input().split()))

result = numbers[0]
for num in numbers[1:]:
    result = mega_nod(result, num)

print(result)
