n = int(input())
list_divisors = []
vulue = n


def divisors(n):
    for i in range(2, int(round(n ** (0.5))) + 1):
        if (n % i) == 0:
            list_divisors.append(i)
            return divisors(n // i)
    list_divisors.append(n)


divisors(n)


def products(divisors):
    result = [1]
    for p in divisors:
        result += [x * p for x in result]
    return result


print(len(set(products(list_divisors))))
