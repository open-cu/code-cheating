import re

input_text = input()
count_of_digits = len(re.findall(r"\d", input_text))
count_of_letters = len(re.findall(r"[a-z]", input_text))
if count_of_digits == count_of_letters == 1:
    print("YES")
else:
    print("NO")
