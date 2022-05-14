from decimal import Clamped


def mergeSortedArrays1(arr1, arr2):
    merged = []

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    if i < len(arr1):
        for x in range(i, len(arr1)):
            merged.append(arr1[x])
    if j < len(arr2):
        for x in range(j, len(arr2)):
            merged.append(arr2[x])

    return merged

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [7]

sorted1 = mergeSortedArrays1(arr1, arr2)

print(sorted1)