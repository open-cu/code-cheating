s = input()

alphabet = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'

if s[0] in alphabet and s[1] in numbers or s[0] in numbers and s[1] in alphabet:
    print('YES')
else:
    print('NO')