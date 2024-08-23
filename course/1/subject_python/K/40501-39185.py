def to_initial_str(s: str) -> str:
    init_str = s
    res_str = []
    i = 0

    while i < len(s):
        digit = ""
        if s[i].isdigit():
            while s[i].isdigit():
                digit += s[i]
                i += 1
            
            res_str.append((int(digit) - 1) * init_str[i])
        else:
            res_str.append(s[i])
            i += 1
    
    return "".join(res_str)


def main() -> None:
    s = input()
    print(to_initial_str(s))


if __name__ == "__main__":
    main()