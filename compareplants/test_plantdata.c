#include <stdio.h>
#include "plantdata.h"


int main () {
    Benefit *benefits = create_benefits();
    printf("created benefits\n");

    printf("first friend of basil is: %d\n", benefits[BASIL].friends[0]);

    free_benefits(benefits);

    printf("Freed!\n");


    return 1;
}
