def is_palindrom(s):
    left_ptr = 0
    right_ptr = len(s) - 1

    while left_ptr <= right_ptr:
        if s[left_ptr] != s[right_ptr]:
            return False
        left_ptr += 1
        right_ptr -= 1

    return True


def is_padable_to_palindrome(s):
    left_ptr = -1
    right_ptr = len(s)

    for i, char in enumerate(s):
        if s[i] != "a" and left_ptr == -1:
            left_ptr = i
        if s[i] != "a":
            right_ptr = i

    if left_ptr == -1:
        return True
    else:
        is_mid_sub_str_palindrom = is_palindrom(s[left_ptr:right_ptr + 1])
        right_a_count = len(s) - 1 - right_ptr
        left_a_count = left_ptr

        if not is_mid_sub_str_palindrom:
            return False
        return left_a_count <= right_a_count


s = input()
print("Yes" if is_padable_to_palindrome(s) else "No")
