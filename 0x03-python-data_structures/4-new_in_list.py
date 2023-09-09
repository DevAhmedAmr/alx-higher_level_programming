#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    
    if my_list== None:
        return
    list_copy = my_list.copy()
    
    if idx < len(my_list):
        list_copy[idx]=element
        
    return list_copy
