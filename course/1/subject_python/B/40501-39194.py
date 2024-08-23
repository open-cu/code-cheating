def fib(n):
    fib_array = [0, 1]
    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])
    return fib_array[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
