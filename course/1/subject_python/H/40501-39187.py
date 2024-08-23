def palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            if s[end] == 'a':
                end -= 1
                continue
            else:
                return False
        start += 1
        end -= 1
    return True


s = input()
if palindrome(s):
    print('YES')
else:
    print('NO')
