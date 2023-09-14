#!/usr/bin/python3
def complex_delete(a_dictionary, value): 
    keys_to_be_deleted=[]
    
    if a_dictionary is None or value is None:
        return None
    
    for i in a_dictionary:
        if a_dictionary[i] == value:
            keys_to_be_deleted.append(i)
            
    if len(keys_to_be_deleted) == 0:
        return a_dictionary
            
    for i in range(len(keys_to_be_deleted)):
        a_dictionary.pop(keys_to_be_deleted[i])
        
    return a_dictionary

