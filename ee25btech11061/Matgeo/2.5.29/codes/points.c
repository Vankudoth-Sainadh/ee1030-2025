// geom.c
#include <stdio.h>

int is_right_at_B(int Ax, int Ay, int Bx, int By, int Cx, int Cy) {
    long BAx = Ax - Bx, BAy = Ay - By;
    long BCx = Cx - Bx, BCy = Cy - By;
    long dot = BAx * BCx + BAy * BCy;
    return dot == 0 ? 1 : 0;
}

int solve_p_for_given_question(void) {
    // A(4,7), B(p,3), C(7,3); right angle at B ⇒ (4-p,4)·(7-p,0)=0 ⇒ p=4
    return 4;
}

