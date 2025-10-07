
#include <math.h>

static void intersect(double a1,double b1,double c1,
                      double a2,double b2,double c2,
                      double *x,double *y)
{
    double D = a1*b2 - a2*b1;
    *x = (b1*(-c2) - b2*(-c1)) / D;
    *y = (a2*(-c1) - a1*(-c2)) / D;
}

// Problem: y=2x+1, y=3x+1, x=4
// In ax+by+c=0 form: -2x + y -1 = 0 ; -3x + y -1 = 0 ; 1x + 0y -4 = 0
double triangle_area_example(void)
{
    double x1,y1,x2,y2,x3,y3;

    // L1 & L2
    intersect(-2, 1, -1,  -3, 1, -1,  &x1,&y1);
    // L2 & L3
    intersect(-3, 1, -1,   1, 0, -4,  &x2,&y2);
    // L3 & L1
    intersect( 1, 0, -4,  -2, 1, -1,  &x3,&y3);

    // Area = 1/2 * |det([B-A, C-A])|
    double ABx = x2 - x1, ABy = y2 - y1;
    double ACx = x3 - x1, ACy = y3 - y1;
    double area = 0.5 * fabs(ABx*ACy - ABy*ACx);
    return area;
}

