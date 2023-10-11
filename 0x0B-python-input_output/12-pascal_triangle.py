#!/usr/bin/python3
""" pascal triangle """



def pascal_triangle(n):
    """12. Pascal's Triangle"""

    list_a =[]
    
    for i in range(1,n+1):
        list_b=[]
        first_indx = 1

        for j in range(i):
            if i <=2:
                list_b.append(1)
            else:
                if (first_indx == 1):
                    list_b.append(1)
                    first_indx = 0
                else:
                    if (j == i-1):
                        list_b.append(1)
                    else :
                        list_b.append(list_a[i-2][j] + list_a[i-2][j-1])

        list_a.append(list_b)
    return list_a
