#include <Python.h>

/**
 * print_python_list_info - prints python list object info
 *
 * @p: pointer to generic PyObject which is of PyListObject type
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size, i = 0;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	while (i < size)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        i++;
	}
}
