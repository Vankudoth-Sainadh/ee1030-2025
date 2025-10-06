import ctypes
from ctypes import c_double, c_int, byref

# Adjust name for macOS if needed: "./liblinegeom.dylib"
lib = ctypes.CDLL("./liblinegeom.so")

lib.line_params.argtypes = [c_double, c_double, c_double,
                            ctypes.POINTER(c_double), ctypes.POINTER(c_int),
                            ctypes.POINTER(c_double), ctypes.POINTER(c_int),
                            ctypes.POINTER(c_double), ctypes.POINTER(c_int)]
lib.line_params.restype  = c_int

lib.example_3m4p10.argtypes = [ctypes.POINTER(c_double), ctypes.POINTER(c_int),
                               ctypes.POINTER(c_double), ctypes.POINTER(c_int),
                               ctypes.POINTER(c_double), ctypes.POINTER(c_int)]
lib.example_3m4p10.restype  = c_int

def run_example():
    slope = c_double(); slope_def = c_int()
    xint  = c_double(); x_def     = c_int()
    yint  = c_double(); y_def     = c_int()

    lib.example_3m4p10(byref(slope), byref(slope_def),
                       byref(xint),  byref(x_def),
                       byref(yint),  byref(y_def))

    print("Line: 3x - 4y + 10 = 0")
    if slope_def.value: print(f"Slope m = {slope.value:.6g}")
    if x_def.value:     print(f"x-intercept = ({xint.value:.6g}, 0)")
    if y_def.value:     print(f"y-intercept = (0, {yint.value:.6g})")

def run_general(a, b, c):
    slope = c_double(); slope_def = c_int()
    xint  = c_double(); x_def     = c_int()
    yint  = c_double(); y_def     = c_int()

    lib.line_params(a, b, c,
                    byref(slope), byref(slope_def),
                    byref(xint),  byref(x_def),
                    byref(yint),  byref(y_def))

    print(f"Line: {a}x + {b}y + {c} = 0")
    if slope_def.value: print(f"Slope m = {slope.value:.6g}")
    else:               print("Slope undefined (vertical line)")
    if x_def.value:     print(f"x-intercept = ({xint.value:.6g}, 0)")
    else:               print("No finite x-intercept (a = 0)")
    if y_def.value:     print(f"y-intercept = (0, {yint.value:.6g})")
    else:               print("No finite y-intercept (b = 0)")

if __name__ == "__main__":
    run_example()
    # run_general(3.0, -4.0, 10.0)

