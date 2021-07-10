def mergeSort(listA) :
    if len(listA) > 1 :
        mid = int(len(listA)/2)
        leftHalf = listA[:mid]
        rightHalf = listA[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0
        while i<len(leftHalf) and j<len(rightHalf) :
            if leftHalf[i] < rightHalf[j] :
                listA[k] = leftHalf[i]
                i = i + 1
            else :
                listA[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i<len(leftHalf) :
            listA[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j<len(rightHalf) :
            listA[k] = rightHalf[j]
            j = j + 1
            k = k + 1

list1 = [4,3,1,5,7,6,8,4]
mergeSort(list1)
print(list1)
