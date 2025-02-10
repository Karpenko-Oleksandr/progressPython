# видалення певного елемента зі списку

def remove_element(element, user_list):
    if element in user_list:
        user_list.remove(element) 
    return user_list

test_list = [1, 2, 3, 4, 3, 5]
result = remove_element(3, test_list)
print(result) 
