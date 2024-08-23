s = input()
s_length = len(s)
s_backwards = s[s_length::-1]
i = 0
k = 0
while i < s_length and s_backwards[i] == 'a':
    i += 1
while k < s_length and s[k] == 'a':
    k += 1
if i >= k:
    s_new = 'a' * i + s[k:]
    new_length = len(s_new)
    if new_length % 2 == 0:
        if s_new[:(new_length//2)] == s_new[(new_length//2):][(new_length//2)::-1]:
            print('Yes')
        else:
            print('No')
    else:
        if s_new[:(new_length//2)] == s_new[(new_length//2) + 1:][(new_length//2) + 1::-1]:
            print('Yes')
        else:
            print('No')
else:
    print("No")