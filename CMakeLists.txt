cmake_minimum_required(VERSION 3.15...3.30)

# Project name comes from SKBUILD_PROJECT_NAME when built via scikit-build-core,
# falling back to a literal name for direct CMake invocations.
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Let pybind11 find Python through CMake's FindPython rather than its own search
set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

# Build the extension module from add.cpp.
# The module name ("basic_math") must match the PYBIND11_MODULE name in add.cpp.
pybind11_add_module(basic_math MODULE src/basic_math/add.cpp)

# Install the compiled .so/.pyd into the Python package directory so that
# scikit-build-core can locate it during the wheel build.
install(TARGETS basic_math DESTINATION ${SKBUILD_PROJECT_NAME})