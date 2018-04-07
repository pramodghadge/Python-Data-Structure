def merge_sort(aList):
    if len(aList) < 2:
        return aList
    mid = len(aList) / 2

    left = merge_sort(aList[:mid])
    right = merge_sort(aList[mid:])

    i = j = 0
    b = []

    while len(b) < len(aList):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            b.append(left[i])
            i += 1
        elif j < len(right):
            b.append(right[j])
            j += 1

    return b


if __name__ == '__main__':
    aList = [23,3,5,34,65,20,10]
    newList = merge_sort(aList)
    print newList