#include "area.h"

int area(struct Point *p1, struct Point *p2)
{
    return abs((p1->x - p2->x) * (p1->y - p2->y));
}
