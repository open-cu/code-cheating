def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


m = int(input())
list_ = input().split(" ")
k = int(list_[0])
for i in range(len(list_)):
    k = gcd(k, int(list_[i]))
print(k)
