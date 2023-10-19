#include <python.h>

/**
 * print_python_string - prints information about Python strings
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	Py_ssize_t length = PyUnicode_GET_LENGTH(p);
	const char *value = PyUnicode_AsUTF8(p);

	printf("  type: compact %s\n",
			PyUnicode_IS_COMPACT_ASCII(p) ? "ascii" : "unicode object");
	printf("  length: %ld\n", length);
	printf("  value: %s\n", value);
}
