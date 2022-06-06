#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print list info
 * @py: pyobject
 */

 void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    PyObject *item;
    int size, i;

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %d\n", size);
    list = (PyListObject *)p;
    printf("[*] Allocated = %d\n", list->allocated)
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name)
    }
}
