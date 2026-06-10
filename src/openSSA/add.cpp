#include <pybind11/pybind11.h>
#include "add.h"

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(_openSSA, m) {
    m.def("add", &add, py::arg("i"), py::arg("j"));
}