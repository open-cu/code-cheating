def max_(a, b):
    diff = a - b - 1
    sign = (diff // abs(diff) + 1) // 2
    return a * sign + b * (1 - sign)


a = int(input())
b = int(input())
print(max_(a, b))
