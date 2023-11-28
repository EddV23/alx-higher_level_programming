#include <Python.h>

/**
 * print_python_string - prints some basic info about Python string
 * @p: PyObject string
 * Return: void
 */
void print_python_string(PyObject *p)
{
	long int size;
	int *str;

	fflush(stdout);
	printf("[.] string object info\n");
	/*if (!PyUnicode_Check(p))*/
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (!PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact unicode object\n");
	else
		printf("  type: compact ascii\n");

	size = ((PyASCIIObject *)(p))->length;
	printf("  length: %ld\n", size);

	str = PyUnicode_AsWideCharString(p, &size);
	printf("  value: %ls\n", str);
}
