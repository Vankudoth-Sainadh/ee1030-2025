import numpy as np
import matplotlib.pyplot as plt
import os

def intersection(a1,b1,c1, a2,b2,c2):
    A = np.array([[a1,b1],[a2,b2]], dtype=float)
    B = np.array([-c1,-c2], dtype=float)
    x, y = np.linalg.solve(A, B)
    return np.array([x, y])

L1 = (-2, 1, -1)
L2 = (-3, 1, -1)
L3 = (1, 0, -4)

A = intersection(*L1, *L2)
B = intersection(*L2, *L3)
C = intersection(*L1, *L3)
V = np.vstack([A,B,C])

x1,y1 = A; x2,y2 = B; x3,y3 = C
area = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
print("Area of the triangle =", area)

xs = np.linspace(min(V[:,0])-1, max(V[:,0])+1, 400)

plt.figure(figsize=(6,6))
plt.plot(xs, 2*xs + 1, color="blue")
plt.plot(xs, 3*xs + 1, color="green")
plt.axvline(4, color="red")
plt.fill([x1,x2,x3],[y1,y2,y3], color="lightblue", alpha=0.5)

for name, P in zip(["A","B","C"], V):
    plt.scatter(P[0], P[1], color="black")
    plt.text(P[0], P[1], f"{name}({P[0]:.1f},{P[1]:.1f})")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Triangle formed by y=2x+1, y=3x+1, x=4")
plt.grid(True)
plt.axis("equal")

os.makedirs("figs", exist_ok=True)
plt.savefig("figs/triangle.png", dpi=200)
plt.show()

