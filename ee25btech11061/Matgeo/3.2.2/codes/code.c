// geom.c  — build a shared lib:  gcc -shared -fPIC -O2 -o libtriangle.so geom.c
#include <math.h>

// Compute coordinates for triangle ABC with B at (0,0), BC along +x.
// Inputs: AB, BC (lengths), angleB_deg (degrees for ∠ABC)
// Outputs (by pointer): Ax,Ay,Bx,By,Cx,Cy and AC length (b_out)
// Returns 0 on success.
int triangle_abc(double AB, double BC, double angleB_deg,
                 double* Ax, double* Ay,
                 double* Bx, double* By,
                 double* Cx, double* Cy,
                 double* b_out)
{
    const double pi = 3.14159265358979323846;
    double B = angleB_deg * (pi/180.0);

    // Place B at origin and C on x-axis
    *Bx = 0.0; *By = 0.0;
    *Cx = BC;  *Cy = 0.0;

    // From B, place A using polar (AB, angle B)
    *Ax = AB * cos(B);
    *Ay = AB * sin(B);

    // b = AC
    double dx = *Ax - *Cx, dy = *Ay - *Cy;
    *b_out = sqrt(dx*dx + dy*dy);

    return 0;
}

// Convenience function for your specific data: AB=5, BC=6, ∠B=60°
int triangle_example(double* Ax, double* Ay,
                     double* Bx, double* By,
                     double* Cx, double* Cy,
                     double* b_out)
{
    return triangle_abc(5.0, 6.0, 60.0, Ax, Ay, Bx, By, Cx, Cy, b_out);
}

