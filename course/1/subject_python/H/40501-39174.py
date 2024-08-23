word = input()
left_a = len(word) - len(word.lstrip('a'))
right_a = len(word) - len(word.rstrip('a'))
stripped = word.lstrip('a').rstrip('a')

if stripped == stripped[::-1] and left_a <= right_a:
    print('Yes')
else:
    print('No')
