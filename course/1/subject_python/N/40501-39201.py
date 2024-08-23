s1 = input()
s2 = input()
result = 'NO'

s = s1 * max(len(s1) // len(s2) + 1, len(s2) // len(s1) + 1)

print('YES' if s2 in s or s2 in ''.join(reversed(s)) else 'NO')
