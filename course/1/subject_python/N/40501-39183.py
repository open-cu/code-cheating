def search(string: str, goal: str) -> str:
    characters = list(string * ((len(goal) + len(string) - 1) // len(string)))

    for start_position in range(len(characters)):
        clockwise = ''.join(characters[start_position:] + characters[:start_position])
        anticlockwise = ''.join(reversed(clockwise))
        if goal in clockwise or goal in anticlockwise:
            return 'YES'
    return 'NO'


string, found = input(), input()
print(search(string, found))
