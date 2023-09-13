#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    
    for element in set_1:
        # Use bitwise AND to check if the element is also in set_2
        if element in set_2:
            common_set.add(element)
    
    return common_set

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

result = common_elements(set1, set2)
print(result)  # Output: {3, 4, 5}