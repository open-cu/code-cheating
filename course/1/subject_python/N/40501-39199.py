def check_start_position(start_pos, cyclic_str, check_word, direction):
    assert direction in {0, 1}, direction
    # 0 clockwise, 1 counter_clockwise

    word_ptr = 0
    cyclic_ptr = start_pos

    while word_ptr < len(check_word):
        if cyclic_ptr == len(cyclic_str):
            cyclic_ptr = 0
        elif cyclic_ptr < 0:
            cyclic_ptr = len(cyclic_str) - 1

        if cyclic_str[cyclic_ptr] == check_word[word_ptr]:
            if direction == 0:
                cyclic_ptr += 1
            elif direction == 1:
                cyclic_ptr -= 1
            word_ptr += 1
        else:
            return False

    return True


def check_cyclic_read(cyclic_str, check_word):
    for i, char in enumerate(cyclic_str):
        if char == check_word[0] and (
            check_start_position(i, cyclic_str, check_word, 0) or check_start_position(i, cyclic_str, check_word, 1)
        ):
            return True

    return False


cyclic_str = input()
check_word = input()
print("YES" if check_cyclic_read(cyclic_str, check_word) else "NO")
