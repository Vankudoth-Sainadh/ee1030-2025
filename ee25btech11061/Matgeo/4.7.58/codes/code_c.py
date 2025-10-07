import ctypes
from ctypes import c_double, Structure

# Adjust filename for macOS: "./libdistlines.dylib"
lib = ctypes.CDLL("./libdistlines.so")

class DistOut(Structure):
    _fields_ = [("distance", c_double),
                ("norm_n",   c_double),
                ("delta_c",  c_double)]

lib.distance_parallel_pack.argtypes = [c_double, c_double, c_double, c_double]
lib.distance_parallel_pack.restype  = DistOut

lib.example_3m4_c7_c5.argtypes = []
lib.example_3m4_c7_c5.restype  = DistOut

# Example for your lines 3x - 4y + 7 = 0 and 3x - 4y + 5 = 0
res = lib.example_3m4_c7_c5()
print("Lines: 3x - 4y + 7 = 0   and   3x - 4y + 5 = 0")
print(f"‖n‖ = {res.norm_n:.6g},  |Δc| = {res.delta_c:.6g}")
print(f"Distance = {res.distance:.6g}")

# General call (uncomment to try other lines with same a,b):
# g = lib.distance_parallel_pack(3.0, -4.0, 7.0, 5.0)
# print(g.distance)

