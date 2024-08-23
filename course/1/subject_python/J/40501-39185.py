from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    _ = int(input())
    numbers = list(map(int, input().split()))

    print(reduce(gcd, numbers))
    

if __name__ == "__main__":
    main()