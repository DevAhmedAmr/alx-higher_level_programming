#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	printf("[*] Size of the Python List = %i", size);
}