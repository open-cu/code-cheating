encoded_word = input()

consecutive_numbers_str = ""
result_str = ""
for symbol in encoded_word:
    if symbol.isdigit():
        consecutive_numbers_str += symbol
    else:
        if not consecutive_numbers_str:
            result_str += symbol
        else:
            result_str += symbol * int(consecutive_numbers_str)
            consecutive_numbers_str = ""

print(result_str)
