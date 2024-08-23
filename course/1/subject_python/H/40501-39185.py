def is_palindrom(s: str) -> str:
    cnt_backward = 0

    for i in s[::-1]:
        if i == 'a':
            cnt_backward += 1
        else:
            break

    cnt_forward = 0
    for i in s:
        if i == 'a':
            cnt_forward += 1
        else:
            break

    s = 'a' * (cnt_backward - cnt_forward) + s

    if s == s[::-1]:
        return "YES"
    return "NO"


def main():
    s = input()
    print(is_palindrom(s))


if __name__ == "__main__":
    main()
