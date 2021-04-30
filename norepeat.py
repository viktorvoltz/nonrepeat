def nonrepeat(sortedList):

    if len(sortedList) == 0:
        return sortedList

    firstIndex = 0
    nextIndex = 1

    print(sortedList[1], sortedList[firstIndex - 1], sortedList[nextIndex], len(sortedList))

    listSize = 1

    while nextIndex < len(sortedList):
        if sortedList[firstIndex] != sortedList[nextIndex]:
            firstIndex = nextIndex
            listSize += 1

        nextIndex += 1

    print(listSize)
    return listSize



arr = [1,2,4,4,5,5,6,6,6,6,6,7,8]
#this example prints seven (7).

nonrepeat(arr)
