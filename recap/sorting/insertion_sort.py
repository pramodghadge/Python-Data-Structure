def insertion_sort(aList):
    for i in range(1, len(aList)):
        insert(aList, i, aList[i])


def insert(aList, idx, value):
    idx -= 1
    while idx >=0 and aList[idx] > value:
        aList[idx+1] = aList[idx]
        idx -= 1
    aList[idx+1] = value

if __name__ == '__main__':
    aList = [23,3,5,34,65,20,10]
    insertion_sort(aList)
    print aList