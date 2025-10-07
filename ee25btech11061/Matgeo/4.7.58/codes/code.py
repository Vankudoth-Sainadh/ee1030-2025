import numpy as np
import matplotlib.pyplot as plt

# Lines: a x + b y + c1 = 0 and a x + b y + c2 = 0
a, b = 3.0, -4.0
c1, c2 = 7.0, 5.0

# Distance formula (same as in C)
norm_n = (a*a + b*b)**0.5
dist = abs(c1 - c2) / norm_n
print(f"Distance = {dist:.6g}")  # should be 2/5 = 0.4

# Solve y = (-a x - c)/b for plotting (b ≠ 0 here)
xs = np.linspace(-6, 6, 400)
y1 = (-a*xs - c1)/b
y2 = (-a*xs - c2)/b

plt.figure(figsize=(6, 6))
plt.plot(xs, y1, linewidth=2, label=r"$3x-4y+7=0$")
plt.plot(xs, y2, linewidth=2, label=r"$3x-4y+5=0$")

# Draw a perpendicular segment between the lines through an easy x (x=0)
x0 = 0.0
y_on_L1 = (-a*x0 - c1)/b
# Perpendicular direction is along n = (a,b); unit vector:
ux, uy = a/norm_n, b/norm_n
# End point on L2 is at distance 'dist' along ±(ux,uy):
x1p = x0 + dist*ux
y1p = y_on_L1 + dist*uy
plt.plot([x0, x1p], [y_on_L1, y1p], linestyle="--", linewidth=2, label="distance")

# Decorations
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distance between 3x-4y+7=0 and 3x-4y+5=0")
plt.tight_layout()
plt.show()

