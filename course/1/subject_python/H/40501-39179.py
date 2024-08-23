def palindrome(s):

    if len(s) % 2 == 1 and s[:len(s) // 2] == (s[len(s) // 2 + 1:])[::-1]:
        return True
    elif len(s) % 2 == 0 and s[:len(s) // 2] == (s[len(s) // 2:])[::-1]:
        return True
    return False


def potential_palindrome(s):
    end = 0
    start = 0
    for i in range(len(s)):
        if s[-(i + 1)] == "a":
            end += 1
        else:
            break

    for i in range(len(s)):
        if s[i] == "a":
            start += 1
        else:
            break

    if palindrome((end - start) * "a" + s):
        print("YES")
    else:
        print("NO")


s = input()
potential_palindrome(s)