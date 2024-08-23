s = input()

right_num_a = len(s) - len(s.rstrip('a'))
left_num_a = len(s) - len(s.lstrip('a'))

if s.endswith('a'):
    s = s.strip('a')

if (s == s[::-1] or s == '') and (right_num_a - left_num_a >= 0):
    print('Yes')
else:
    print('No')
