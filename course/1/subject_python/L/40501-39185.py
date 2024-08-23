def non_decreasing(arr):
    tmp = float('-inf')

    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    for j in range(len(arr)):
        if -arr[j] >= tmp:
            arr[j] = -arr[j]
        if arr[j] < tmp:
            return "No"
        tmp = arr[j]

    return "Yes"


def main() -> None:
    _ = int(input())
    arr = list(map(int, input().split()))

    label = non_decreasing(arr)
    if label == "Yes":
        print(label)
        print(*arr)
    else:
        print(label)


if __name__ == "__main__":
    main()
