// Build (Linux):  gcc -shared -fPIC -O2 -o liblinegeom.so linegeom.c
// Build (macOS):  clang -dynamiclib -O2 -o liblinegeom.dylib linegeom.c
#include <math.h>

// ax + by + c = 0  → slope = -a/b (if b ≠ 0)
// x-intercept = (-c/a, 0) if a ≠ 0
// y-intercept = (0, -c/b) if b ≠ 0
int line_params(double a, double b, double c,
                double* slope, int* slope_defined,
                double* xint,  int* x_defined,
                double* yint,  int* y_defined)
{
    if (b != 0.0) { *slope = -a/b; *slope_defined = 1; }
    else          { *slope = NAN;  *slope_defined = 0; }

    if (a != 0.0) { *xint = -c/a;  *x_defined = 1; }
    else          { *xint = NAN;   *x_defined = 0; }

    if (b != 0.0) { *yint = -c/b;  *y_defined = 1; }
    else          { *yint = NAN;   *y_defined = 0; }

    return 0;
}

// Convenience: for 3x - 4y + 10 = 0
int example_3m4p10(double* slope, int* slope_defined,
                   double* xint,  int* x_defined,
                   double* yint,  int* y_defined)
{
    return line_params(3.0, -4.0, 10.0,
                       slope, slope_defined,
                       xint,  x_defined,
                       yint,  y_defined);
}

