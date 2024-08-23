def is_pal(s: str, padding="a"):
    l, r = 0, len(s) - 1

    once = False

    while r - l >= 1:
        if s[l] == s[r]:
            if s[l] != padding:
                once = True

            l += 1
            r -= 1
        elif not once and s[r] == padding:
            r -= 1
        else:
            return False

    return True


def solution():
    s = input()

    print("Yes" if is_pal(s) else "No")


solution()
