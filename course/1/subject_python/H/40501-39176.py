def solution(text: str) -> str:
    counter = 0
    left = 0
    while left < len(text) and text[left] == 'a':
        left += 1
        counter += 1
    right = len(text) - 1
    while right >= 0 and text[right] == 'a':
        right -= 1
        counter -= 1

    if counter > 0:
        return 'No'
    stripped_text = text[max(left, 0):min(right + 1, len(text))]

    if len(stripped_text) % 2 == 1:
        left = right = len(stripped_text) // 2
    else:
        right = len(stripped_text) // 2
        left = right - 1
    while left >= 0:
        if stripped_text[left] != stripped_text[right]:
            return 'No'
        left -= 1
        right += 1
    return 'Yes'


print(solution(input()))
