def solution(text: str, word: str) -> str:
    def check_contain(text_: str, word_: str) -> bool:
        for i in range(len(text_) - len(word)):
            for j in range(len(word_)):
                if word_[j] != text_[i + j]:
                    break
            else:
                return True
        return False

    text = text * (len(word) // len(text) + 2)
    if check_contain(text, word):
        return 'YES'
    text = text[::-1]
    return 'YES' if check_contain(text, word) else 'NO'


print(solution(input(), input()))
