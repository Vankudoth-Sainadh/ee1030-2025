# use_geom.py
import ctypes
from ctypes import c_int

lib = ctypes.CDLL("./libgeom.so")

lib.is_right_at_B.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int]
lib.is_right_at_B.restype  = c_int

lib.solve_p_for_given_question.argtypes = []
lib.solve_p_for_given_question.restype  = c_int

p = lib.solve_p_for_given_question()
print(p)

ok = lib.is_right_at_B(4, 7, p, 3, 7, 3)
print("RIGHT" if ok else "NOT_RIGHT")

