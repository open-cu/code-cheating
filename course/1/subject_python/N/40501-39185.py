def find_substring(initital_string, substring):
    if substring in initital_string or substring in initital_string[::-1]:
        return "YES"
    return "NO"


def main() -> None:
    initital_string = input()
    substring = input()
    initital_string_len = len(initital_string)
    substring_len = len(substring)

    if substring_len > initital_string_len * 2:
        initital_string = substring_len // initital_string_len * initital_string
    else:
        initital_string = 2 * initital_string

    is_entrying = find_substring(initital_string, substring)
    print(is_entrying)


if __name__ == "__main__":
    main()
