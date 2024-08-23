def count_streaks(arr):
    streaks = []

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            continue
        else:
            streaks.append(arr[i - 1])
        
    streaks.append(arr[i])
    return streaks


def main() -> None:
    _ = int(input())
    arr = list(map(int, input().split()))

    streaks = count_streaks(arr)
    print(len(streaks))
    print(*streaks)
    

if __name__ == "__main__":
    main()
    