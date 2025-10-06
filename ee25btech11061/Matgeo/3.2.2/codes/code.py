# plot_triangle.py — direct Python to compute and PLOT your triangle
# AB=5 cm, BC=6 cm, angle ABC=60°
import math
import matplotlib.pyplot as plt

AB = 5.0
BC = 6.0
Bdeg = 60.0
Brad = math.radians(Bdeg)

# Coordinates: place B at origin and C on +x as in your LaTeX
Bx, By = 0.0, 0.0
Cx, Cy = BC, 0.0
Ax, Ay = AB*math.cos(Brad), AB*math.sin(Brad)  # (2.5, 4.330...)

# Optional: AC to confirm = sqrt(31)
AC = math.hypot(Ax-Cx, Ay-Cy)

# Plot
plt.figure(figsize=(5,5))
# triangle edges
plt.plot([Ax, Bx], [Ay, By])  # AB
plt.plot([Bx, Cx], [By, Cy])  # BC
plt.plot([Cx, Ax], [Cy, Ay])  # CA

# points
plt.scatter([Ax, Bx, Cx], [Ay, By, Cy])
plt.text(Ax, Ay, f"  A({Ax:.2f},{Ay:.2f})", ha="left", va="bottom")
plt.text(Bx, By, f"  B({Bx:.2f},{By:.2f})", ha="left", va="top")
plt.text(Cx, Cy, f"  C({Cx:.2f},{Cy:.2f})", ha="left", va="top")

plt.title("Triangle ABC (AB=5, BC=6, ∠ABC=60°)")
plt.axis("equal")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
# Save and/or show
plt.savefig("triangle_abc.png", dpi=200)
plt.show()
print(f"AC ≈ {AC:.4f} (should be sqrt(31) ≈ 5.5678)")

