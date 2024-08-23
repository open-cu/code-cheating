n = int(input())

temp_dict = {}


def fibonacci_recursive(n):
    if n in temp_dict:
        return temp_dict[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp_dict[n] = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    return temp_dict[n]


print(fibonacci_recursive(n))
