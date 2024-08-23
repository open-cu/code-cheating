def main():
    s1, s2 = list(input())

    if (s1.isdigit() or s2.isdigit()) and (s1.isalpha() or s2.isalpha()):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()