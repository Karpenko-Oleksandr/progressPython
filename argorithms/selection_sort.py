def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# test
my_array = [5, 22, 3335, 1, 9]
print(findSmallest(my_array))


def selectionSort(arr):
    new_arr = []
    
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


# test
print(selectionSort(my_array))