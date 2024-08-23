def isPalindrome(s, begin, end):
    while begin < end:
        if s[begin] != s[end]:
            return False
        begin += 1
        end -= 1
    return True


s = input()
i = 0
j = len(s) - 1
a_count_start = 0
a_count_end = 0

while i < len(s) and s[i] == 'a':
    i += 1
    a_count_start += 1

while j >= 0 and s[j] == 'a':
    j -= 1
    a_count_end += 1

if a_count_start > a_count_end:
    print('No')
else:
    print('Yes' if isPalindrome(s, i, j) else 'No')
