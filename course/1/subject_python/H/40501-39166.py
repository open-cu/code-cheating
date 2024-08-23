def is_palindrome(s):
    return s == s[::-1]


s = input()
if is_palindrome(s):
    print('Yes')
elif is_palindrome(s.strip('a')) and len(s.lstrip('a')) > len(s.rstrip('a')):
    print('Yes')
else:
    print('No')
