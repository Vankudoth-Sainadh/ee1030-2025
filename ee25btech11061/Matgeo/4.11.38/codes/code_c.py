import ctypes
from ctypes import c_double
import os, sys

# Pick correct lib name
libname = "libsimple_triarea.dylib" if sys.platform == "darwin" else "libsimple_triarea.so"
lib = ctypes.CDLL(os.path.abspath(libname))

# C function: double triangle_area_example(void)
lib.triangle_area_example.restype = c_double

area = lib.triangle_area_example()
print(f"Area of the triangle (y=2x+1, y=3x+1, x=4) = {area}")

