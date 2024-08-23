def nth_fibonacci(n):
    prev, curr = 0, 1

    for _ in range(n):
        prev, curr = curr, prev + curr

    return prev


def main():
    n = int(input())
    print(nth_fibonacci(n))


if __name__ == "__main__":
    main()