def is_prime(n):

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return "composite"
    return "prime"


def main():
    n = int(input())
    print(is_prime(n))
    

if __name__ == "__main__":
    main()