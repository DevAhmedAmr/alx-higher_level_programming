#!/usr/bin/python3
""" pascal triangle """
def pascal_triangle(n):
    """ pascal triangle """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles

# def pascal_triangle(n):
#     list_a =[]
#     for i in range(1,n+1):
#         list_b=[]
#         for j in range(i):
#             if i <=2:
#                 list_b.append(1)

#         list_a.append(list_b)


# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


# if __name__ == "__main__":
#     print_triangle(pascal_triangle(5))
