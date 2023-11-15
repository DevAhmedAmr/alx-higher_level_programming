#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """12. Pascal's Triangle"""

    list_a = []

    for i in range(1, n+1):
        list_b = []

        for j in range(0, i):
            if i <= 2:
                list_b.append(1)
            else:
                # start index
                if (j == 0):
                    list_b.append(1)

                else:
                    # last index
                    if (j == i-1):
                        list_b.append(1)

                    else:
                        # print(">>>>>>>> {}".format(j))
                        # print("    >>>>>> {}".format(list_a[i-2]))
                        # print("    >>>>>> {} + {} ".format(list_a[i-2][j-1],
                        # list_a[i-2][j] ))
                        # print("------")
                        list_b.append(list_a[i-2][j-1] + list_a[i-2][j])

        list_a.append(list_b)
    return list_a


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
