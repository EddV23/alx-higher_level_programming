#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	/*Py_ssize_t size, i;*/
	long int size, i;
	PyListObject *alloc;
	PyObject *obj;

	size = PyList_Size(p);
	/*size = ((PyVarObject *)(p))->ob_size;*/
	alloc = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	/*Py_ssize_t size, i, delim;*/
	long int size, i, delim;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	/*printf("  first %ld bytes:", size < 10 ? size + 1 : 10);*/
	if (size < 10)
		delim = size + 1;
	else
		delim = 10;
	printf(" first %ld bytes:", delim);

	for (i = 0; i < delim; i++)
	{
		if (str[i] < 0)
			printf(" %02x", 256 + str[i]);
		else
			printf(" %02x", str[i]);
	}
	printf("\n");
}
