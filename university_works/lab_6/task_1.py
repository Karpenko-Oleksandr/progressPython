# додавання елемента перед елементом з визначеним значенням

def add_element_before_defined_element(element, user_list):
    if element in user_list:
        index = user_list.index(element) 
        user_list.insert(index, 18)   
    return user_list

test_list = [1, 2, 3, 4, 5]
result = add_element_before_defined_element(3, test_list)
print(result)
