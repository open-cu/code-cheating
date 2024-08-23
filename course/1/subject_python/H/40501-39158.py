s = input()


def is_palindrom(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if s[j] != 'a':
                return "No"
            else:
                i -= 1
        i += 1
        j -= 1
    return "Yes"


print(is_palindrom(s))
