def my_max(a, b):
    f1 = a // b
    f2 = b // a

    return (f1 * a + f2 * b) // (f1 + f2)


a = int(input())
b = int(input())

print(my_max(a, b))
