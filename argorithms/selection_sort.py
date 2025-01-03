def findSmallest(arr):
    smallest_number = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_number:
            smallest_number = arr[i]
            smallest_index = i
    return smallest_index

# test
my_array = [5, 2, 35, 1, 9]
print(findSmallest(my_array))


def selectionSort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallets_number = findSmallest(arr)
        new_arr.append(arr.pop(smallets_number))
    return new_arr

# test
print(selectionSort(my_array))