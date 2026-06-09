#include <pybind11/pybind11.h>

namespace py = pybind11;

/// Add two integers.
int add(int i, int j) {
    return i + j;
}

// The first argument to PYBIND11_MODULE must match the CMake target name
// ("basic_math") and the name used in Python imports.
PYBIND11_MODULE(basic_math, m) {
    m.doc() = "basic_math: a minimal pybind11 example module";

    m.def("add", &add,
          py::arg("i"), py::arg("j"),
          R"pbdoc(
              Add two integers and return the result.

              Parameters
              ----------
              i : int
                  First operand.
              j : int
                  Second operand.

              Returns
              -------
              int
                  i + j
          )pbdoc");
}