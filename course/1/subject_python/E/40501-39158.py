n = int(input())


def check_ease(n):
    if n == 2:
        return "prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "composite"
    return "prime"


print(check_ease(n))