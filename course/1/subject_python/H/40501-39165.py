def check_palindrom(s):
    for i in range(1, len(s) // 2 + 1):
        if s[i - 1] != s[-i]:
            return False
    return True


s = input()
print('Yes' if check_palindrom(s.strip('a')) & (len(s.lstrip('a')) - len(s.rstrip('a')) >= 0) else 'No')
