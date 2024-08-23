def next_pos(current: int, characters_length: int, reverse: bool) -> int:
    if not reverse:
        return (current + 1) % characters_length
    else:
        return current - 1 if current > 0 else characters_length - 1


def contains_word_from_pos(characters: str, word: str, current_index: int, reverse: bool) -> bool:
    for j in range(len(word)):
        if characters[current_index] == word[j]:
            current_index = next_pos(current_index, len(characters), reverse)
        else:
            return False

    return True


def word_finder() -> bool:
    characters = input()
    word = input()

    for i in range(len(characters)):
        if contains_word_from_pos(characters, word, i, False):
            return True

        if contains_word_from_pos(characters, word, i, True):
            return True

    return False


if __name__ == '__main__':
    print('YES' if word_finder() else 'NO')
