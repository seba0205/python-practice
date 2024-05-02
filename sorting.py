import random

test_array = [random.randint(1, 30) for i in range(30)]


def bubble_sort(array):
    """Implementation of bubble sort"""
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array


def merge_sort(array):
    """Implementation of merge sort"""
    if len(array) == 1:
        return array
    midpoint = len(array) // 2
    return merge(merge_sort(array[:midpoint]), merge_sort(array[midpoint:]))


def merge(array1, array2):
    """Merge + compare function for merge sort"""
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1
    result =[]
    i_left = i_right = 0
    while len(result) < len(array1) + len(array2):
        if array1[i_left] <= array2[i_right]:
            result.append(array1[i_left])
            i_left += 1
        else:
            result.append(array2[i_right])
            i_right += 1

        if i_left == len(array1):
            result += array2[i_right:]

        if i_right == len(array2):
            result += array1[i_left:]

    return result


print(test_array)
print(sorted(test_array))
print(merge_sort(test_array))
