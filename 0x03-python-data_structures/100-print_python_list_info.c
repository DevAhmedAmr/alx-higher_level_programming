#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	(void)Py_SIZE(p);
}