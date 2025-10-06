# use_ctypes.py — Python that loads the .so and prints results
# Build first: gcc -shared -fPIC -O2 -o libtriangle.so geom.c
import ctypes
from ctypes import c_double, c_int, byref

lib = ctypes.CDLL("./libtriangle.so")   # adjust path if needed

# void-return (int), args: 11 doubles (3 inputs + 7 outputs)
lib.triangle_abc.argtypes = [c_double, c_double, c_double,
                             ctypes.POINTER(c_double), ctypes.POINTER(c_double),
                             ctypes.POINTER(c_double), ctypes.POINTER(c_double),
                             ctypes.POINTER(c_double), ctypes.POINTER(c_double),
                             ctypes.POINTER(c_double)]
lib.triangle_abc.restype  = c_int

lib.triangle_example.argtypes = [ctypes.POINTER(c_double), ctypes.POINTER(c_double),
                                 ctypes.POINTER(c_double), ctypes.POINTER(c_double),
                                 ctypes.POINTER(c_double), ctypes.POINTER(c_double),
                                 ctypes.POINTER(c_double)]
lib.triangle_example.restype  = c_int

def run_example():
    Ax= c_double(); Ay= c_double()
    Bx= c_double(); By= c_double()
    Cx= c_double(); Cy= c_double()
    b = c_double()

    lib.triangle_example(byref(Ax), byref(Ay), byref(Bx), byref(By),
                         byref(Cx), byref(Cy), byref(b))

    print("Example (AB=5, BC=6, ∠B=60°)")
    print(f"A = ({Ax.value:.2f}, {Ay.value:.2f})")
    print(f"B = ({Bx.value:.2f}, {By.value:.2f})")
    print(f"C = ({Cx.value:.2f}, {Cy.value:.2f})")
    print(f"AC = sqrt(31) ≈ {b.value:.2f}")

def run_general(AB=5.0, BC=6.0, angleB_deg=60.0):
    Ax= c_double(); Ay= c_double()
    Bx= c_double(); By= c_double()
    Cx= c_double(); Cy= c_double()
    b = c_double()

    lib.triangle_abc(AB, BC, angleB_deg,
                     byref(Ax), byref(Ay),
                     byref(Bx), byref(By),
                     byref(Cx), byref(Cy),
                     byref(b))

    print(f"General AB={AB}, BC={BC}, ∠B={angleB_deg}°")
    print(f"A = ({Ax.value:.4f}, {Ay.value:.4f})")
    print(f"B = ({Bx.value:.4f}, {By.value:.4f})")
    print(f"C = ({Cx.value:.4f}, {Cy.value:.4f})")
    print(f"AC = {b.value:.4f}")

if __name__ == "__main__":
    run_example()
    # run_general()  # or pass custom values

