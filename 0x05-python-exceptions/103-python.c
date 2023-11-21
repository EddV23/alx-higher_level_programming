#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject list
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *alloc;
	PyObject *obj;

	fflush(stdout);
	size = ((PyVarObject *)(p))->ob_size;
	alloc = (PyListObject *)p;
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		/*if (PyBytes_Check(obj))*/
		if (!strcmp((obj)->ob_type->tp_name, "bytes"))
			print_python_bytes(obj);
		/*if (PyFloat_Check(obj))*/
		else if (!strcmp((obj)->ob_type->tp_name, "float"))
			print_python_float(obj);
	}
}

/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: PyObject bytes
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size, delim, i;
	char *str;

	fflush(stdout);
	printf("[.] bytes object info\n");
	/*if (!PyBytes_Check(p))*/
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		delim = size + 1;
	else
		delim = 10;
	printf("  first %ld bytes:", delim);

	for (i = 0; i < delim; i++)
	{
		if (str[i] < 0)
			printf(" %02x", 256 + str[i]);
		else
			printf(" %02x", str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float
 * @p: PyObject float
 * Return: void
 */
void print_python_float(PyObject *p)
{
	char *str = NULL;
	double obj = ((PyFloatObject *)p)->ob_fval;

	fflush(stdout);
	printf("[.] float object info\n");
	/*if (!PyFloat_Check(p))*/
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str = PyOS_double_to_string(obj, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf(" value: %s\n", str);
}
