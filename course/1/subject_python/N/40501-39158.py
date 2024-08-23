s1 = input()
s2 = input()


def check_string(s1, s2):

    if len(s1) == 1:
        for char in s2:
            if char != s1:
                return "NO"
            else:
                return "YES"

    double_s1 = s1 * 2
    reverse_s1 = double_s1[::-1]

    if double_s1.find(s2) != -1:
        return "YES"
    elif reverse_s1.find(s2) != -1:
        return "YES"
    else:
        return "NO"


print(check_string(s1, s2))
