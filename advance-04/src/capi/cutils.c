#include "stdio.h"
#include "stdlib.h"

#include <Python.h>

// sum([1,2,3,4,5], 5)
PyObject* cutils_sum(PyObject *self, PyObject* args)
{
    PyObject* py_list;
    long max_len;
    if (!PyArg_ParseTuple(args, "Ol", &py_list, &max_len))
    {
        printf("ERROR: Failed to parse arguments");
        return NULL;
    }

    long len = PyList_Size(py_list);
    //printf("DEBUG: len of input list is %ld", len);
    long res = 0;
    for (int i = 0; i < len && i < max_len; ++i)
    {
        PyObject *tmp = PyList_GetItem(py_list, i);
        res += PyLong_AsLong(tmp);
    }
    return Py_BuildValue("i", res);
}

int fibonacci(int n)
{
    if (n < 2)
        return 1;
    return fibonacci(n-2) + fibonacci(n-1);
}

PyObject* cutils_fibonacci(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }
    return Py_BuildValue("i", fibonacci(n));
}

PyObject* cutils_dummy(PyObject* self, PyObject* args)
{
    return Py_BuildValue("[i, i]", 100, 500);
}

static PyMethodDef methods[] = {
    { "sum", cutils_sum, METH_VARARGS, "sum of elements of a list." },
    { "fibonacci", cutils_fibonacci, METH_VARARGS, "execute n-th number of Fibonacci sequence." },
    { "dummy", cutils_dummy, METH_NOARGS, "return list of two integers." },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef cutilsmodule =
{
    PyModuleDef_HEAD_INIT, "cutils", NULL, -1, methods
};

PyMODINIT_FUNC PyInit_cutils(void) {
    return PyModule_Create( &cutilsmodule );
}
