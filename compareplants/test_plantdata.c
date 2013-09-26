#include <stdio.h>
#include "plantdata.h"


int main () {
    Benefit *benefits = create_benefits();
    printf("created benefits\n");

    printf("first friend of apple is: %d\n", benefits[APPLE].friends[0]);
    printf("last friend of apple is: %d\n", benefits[APPLE].friends[29]);

    free_benefits(benefits);

    printf("Freed!\n");


    return 1;
}
