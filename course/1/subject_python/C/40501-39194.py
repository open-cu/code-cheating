def delitel(n, m):
    return (m % n == 0 or n % m == 0) * 1


def main():
    n = int(input())
    m = int(input())
    print(delitel(n, m))


if __name__ == "__main__":
    main()
