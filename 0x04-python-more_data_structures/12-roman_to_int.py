#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    roman_dic = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string is None or type(roman_string) != str:
        return None
    
    for i in roman_string:
        if roman_dic.get(i) is not None:
            number += roman_dic[i]
            
    return number


