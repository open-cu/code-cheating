#solution.py
def main() -> None:
    n = int(input())
    m = int(input())
    for i in range(n):
        for j in range(m):
            a = min(i + j, n)
            b = max(0, i + j - m + 1)
            print((a * (a + 1) + (j + i - a) * 2 * n) // 2 + i - b * (b + 1) // 2, end=' ')
        print()

if __name__ == "__main__":
    main()