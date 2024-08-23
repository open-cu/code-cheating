def absolutemax(a, b):
    ind1 = a // b
    ind1 = ((ind1 + 2) // (ind1 + 1)) % 2
    ind2 = (ind1 + 1) % 2
    result = a * ind1 + b * ind2
    return result


n1 = int(input())
n2 = int(input())
print(absolutemax(n1, n2))
