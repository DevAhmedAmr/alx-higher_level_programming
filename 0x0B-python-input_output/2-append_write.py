#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a") as file:
        return file.write(text)
    
nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
