def main():
    a = int(input())
    b = int(input())

    if a % b == 0 or b % a == 0:
        print(1)
    else:
        print(0)
    

if __name__ == "__main__":
    main()