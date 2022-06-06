#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print list info
 * @py: pyobject
 */

 void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    PyObject *item;
    long int size, i;

    size = PyList_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);
    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated)
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name)
    }
}
