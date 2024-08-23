s = input()

n = len(s)
num_a_left = 0
num_a_right = 0
for num_a_left, letter_left in enumerate(s):
    if (letter_left != 'a'):
        break
for num_a_right, letter_right in enumerate(s[::-1]):
    if (letter_right != 'a'):
        break

if (num_a_right >= num_a_left and letter_right == letter_left):
    for i in range((n - num_a_left - num_a_right) // 2):
        if (s[num_a_left + i] != s[n - num_a_right - 1 - i]):
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')
