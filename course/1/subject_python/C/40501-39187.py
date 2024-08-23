def delim(a, b):
    diff = a - b + 1
    sign = (diff // abs(diff) + 1) // 2
    return ((a * sign + b * (1 - sign)) % (a * (1 - sign) + b * sign)) + 1


a = int(input())
b = int(input())
print(delim(a, b))
