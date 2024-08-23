#solution.py
def main() -> None:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if a == 0:
        print("INF" if b == 0 else "NO")
    elif b == 0:
        print(0)
    elif b % a == 0 and -b // a * c + d != 0:
        print(-b // a)
    else:
        print("NO")

if __name__ == "__main__":
    main()