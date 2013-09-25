#include <Python.h>
#include "permutations.h"

static PyObject *compare(PyObject *self, PyObject *args) {
    char *plants;
    int size;
    char *info;

    if (!PyArg_ParseTuple(args, "i", &size))
        return NULL;

    Py_BEGIN_ALLOW_THREADS
    // do threading here


    Py_END_ALLOW_THREADS
    return Py_BuildValue("i", size);
}


static PyMethodDef CompareMethods[] = {
    {"compare",  compare, METH_VARARGS,
        "Compares possible CPC plant layouts."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initcompareplants(void) {
    (void) Py_InitModule("compareplants", CompareMethods);
}



