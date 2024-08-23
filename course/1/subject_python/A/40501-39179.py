def checking_string(s):
    digit_flag = False
    letter_flag = False

    for let in s:
        if let.isdigit():
            digit_flag = True
        elif let.isalpha():
            letter_flag = True

    if digit_flag and letter_flag:
        print("YES")
    else:
        print("NO")


s = input()
checking_string(s)