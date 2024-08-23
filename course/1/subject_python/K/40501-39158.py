s = input()


def reverse_word(s):
    new_s = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = ''
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            if i < len(s):
                new_s.append(s[i] * int(num))
                i += 1
        else:
            new_s.append(s[i])
            i += 1
    return ''.join(new_s)


print(reverse_word(s))
