def count_repeating_a(s: str, index_generator) -> int:
    a_count = 0
    for i in index_generator:
        if s[i] == 'a':
            a_count += 1
        else:
            break

    return a_count


def classic_palindrome(s: str) -> bool:
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-(i + 1)]:
            return False

    return True


def palindrome_with_a(palindrome_candidate):
    a_start_count = count_repeating_a(palindrome_candidate, range(len(palindrome_candidate)))
    a_end_count = count_repeating_a(palindrome_candidate, reversed(range(len(palindrome_candidate))))

    if a_start_count > a_end_count:
        print('No')
        return

    palindrome_candidate = palindrome_candidate.strip('a')

    if len(palindrome_candidate) < 2:
        print('Yes')
        return

    print('Yes' if classic_palindrome(palindrome_candidate) else 'No')


user_input = input()
palindrome_with_a(user_input)
