def palindrome(word: str) -> str:
    inner_word = word.strip('a')
    if inner_word == '':
        return 'Yes'
    else:
        first_point = 0
        while word[first_point] == 'a':
            first_point += 1

        second_point = -1
        while word[second_point] == 'a':
            second_point -= 1

        inner_word = word.strip('a')

        if inner_word == inner_word[::-1] and first_point < abs(second_point):
            return 'Yes'
        else:
            return 'No'


test = input()
print(palindrome(test))
