#!/usr/bin/python3
"""class """


class MyList(list):
    """class """

    def print_sorted(self):
        listCpy = list()
        listCpy.extend(self)
        listCpy.sort()
        print(listCpy)
