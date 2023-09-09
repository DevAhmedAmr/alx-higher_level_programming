#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list)):
        return my_list
    
    if(idx==None):
        return my_list
    
    if(my_list==None):
        return None
    
    if element ==None:
        return my_list
    
    for i in range(len(my_list)):
        if (i == idx):
            my_list[i] = element
            return my_list
