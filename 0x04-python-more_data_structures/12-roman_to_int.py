#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    prev = 0
    roman_dic = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    
    if not roman_string  or type(roman_string) != str:
        return None
    
    for i in  range(len(roman_string)):
        
            
            curr = roman_dic[roman_string[i]]
            
            if prev < curr:
                
                number += curr - 2 * prev
            else:
                
                number += curr
                
            prev = curr
            
    return number
