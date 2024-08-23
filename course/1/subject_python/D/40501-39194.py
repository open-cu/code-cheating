def maximum(n, m):
    return (n // m == 0) * m + (m // n == 0) * n + (m == n) * n


def main():
    n = int(input())
    m = int(input())
    print(maximum(n, m))


if __name__ == "__main__":
    main()
