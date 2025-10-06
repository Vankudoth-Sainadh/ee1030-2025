import numpy as np
import matplotlib.pyplot as plt

# Line: 3x - 4y + 10 = 0  →  y = (3/4)x + 10/4
a, b, c = 3.0, -4.0, 10.0

# Compute intercepts (if defined)
x_int = -c/a if a != 0 else None   # (-10/3, 0)
y_int = -c/b if b != 0 else None   # (0,  2.5)

# Choose a plotting window around intercepts
xs = np.linspace(-10, 10, 400)
if b != 0:
    ys = (-a*xs - c) / b
else:
    # vertical line x = -c/a
    xs = np.full_like(xs, -c/a)
    ys = np.linspace(-10, 10, 400)

plt.figure(figsize=(6, 6))

# Plot the line
plt.plot(xs, ys, linewidth=2)
plt.title("3x - 4y + 10 = 0")

# Axes crosshairs
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

# Mark intercepts if present
if x_int is not None:
    plt.scatter([x_int], [0], s=40)
    plt.text(x_int, 0, f"  x-int=({x_int:.2f}, 0)", va="bottom")

if y_int is not None:
    plt.scatter([0], [y_int], s=40)
    plt.text(0, y_int, f"  y-int=(0, {y_int:.2f})", va="bottom")

plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.tight_layout()
plt.show()

