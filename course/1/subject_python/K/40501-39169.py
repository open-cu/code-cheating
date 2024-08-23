str_ = input()
list_ = list(str_)
count = 0
value = 0
h = 0
ch = 0
for i in range(len(list_)):
    if not (list_[i].isdigit()):
        h = 0
    elif list_[i].isdigit() and list_[i + 1].isdigit():
        value = value + int(list_[i]) * 10 + int(list_[i + 1])
        h = 1
        ch += 1
    elif list_[i].isdigit() and h == 0:
        count += 1
        value = value + int(list_[i])
        h = 0
h = 0
for i in range(len(list_) + value - count * 2 - ch * 3 - 1):
    if not (list_[i].isdigit()):
        h = 0
    elif list_[i].isdigit() and list_[i + 1].isdigit():
        k = int(list_[i]) * 10 + int(list_[i + 1])
        for j in range(0, k - 3):
            list_[i] = list_[i + 2 + j]
            list_.insert(i, list_[i + 2 + j])
        list_[i + k - 2] = list_[i + k - 3]
        h = 1
    elif list_[i].isdigit() and h == 0:
        k = int(list_[i])
        if k <= 2:
            list_[i] = list_[i + 1]
        if k > 2:
            for j in range(0, k - 2):
                list_[i] = list_[i + 1]
                list_.insert(i, list_[i + 1])
print("".join(list_))
