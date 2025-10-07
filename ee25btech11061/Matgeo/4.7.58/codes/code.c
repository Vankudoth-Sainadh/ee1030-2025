
#include <math.h>

typedef struct {
    double distance;   // |c1 - c2| / sqrt(a^2 + b^2)
    double norm_n;     // sqrt(a^2 + b^2)
    double delta_c;    // |c1 - c2|
} DistOut;

// Distance between parallel lines: a x + b y + c1 = 0  and  a x + b y + c2 = 0
DistOut distance_parallel_pack(double a, double b, double c1, double c2) {
    DistOut out;
    out.norm_n  = sqrt(a*a + b*b);
    out.delta_c = fabs(c1 - c2);
    out.distance = (out.norm_n > 0.0) ? (out.delta_c / out.norm_n) : NAN;
    return out;
}

// Convenience for your lines: 3x - 4y + 7 = 0  and  3x - 4y + 5 = 0
DistOut example_3m4_c7_c5(void) {
    return distance_parallel_pack(3.0, -4.0, 7.0, 5.0);
}

