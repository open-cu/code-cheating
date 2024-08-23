s = input()

if s == s[::-1]:
    print('YES')
    
elif 'a' in s:
    cnt_first_a = 0
    n = 0
    
    while s[n] == 'a':
        cnt_first_a += 1
        n += 1
        
    cnt_last_a = 0
    n = 1
    while s[-n] == 'a':
        cnt_last_a += 1
        n += 1
    
    cnt_add_a = cnt_last_a - cnt_first_a
    
    new_s = 'a'*cnt_add_a + s
    
    if new_s == new_s[::-1]:
        print('YES')
    else:
        print('NO')

else:
    print('NO')