# об'єднання двох списків

def merge_lists(list1, list2):
    return list1 + list2 

list_a = [1, 2, 3]
list_b = [4, 5, 6]
result = merge_lists(list_a, list_b)
print(result)  # [1, 2, 3, 4, 5, 6]