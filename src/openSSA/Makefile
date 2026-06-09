PYTHON     := python3
CXX        := g++
PYBIND_INC := $(shell $(PYTHON) -m pybind11 --includes)
EXT_SUFFIX := $(shell $(PYTHON) -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))")
TARGET     := _openSSA$(EXT_SUFFIX)

CXXFLAGS := -O2 -std=c++17 -fPIC -shared $(PYBIND_INC)

$(TARGET): add.cpp add.h
	$(CXX) $(CXXFLAGS) add.cpp -o $(TARGET)

clean:
	rm -f $(TARGET)