names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)

sentence = "Hello, this is a sentence."

no_spaces = sentence.replace(" ", "")

print(no_spaces)

sentence = "Hello, this is a sentence."

num_spaces = sentence.count(" ")

print(f"There are {num_spaces} spaces in the sentence.")


def is_palindrome(word):
    if word == word[::-1]:
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")


is_palindrome("redivider")
