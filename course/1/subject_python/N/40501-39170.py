def letters_circle(circle: str, word: str) -> str:
    circle = circle * len(word)
    if word in circle or word in ''.join(reversed(circle)):
        return 'Yes'
    else:
        return 'No'


circle_test, word_test = input(), input()
print(letters_circle(circle_test, word_test))
