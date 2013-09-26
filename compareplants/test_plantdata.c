#include <stdio.h>
#include "plantdata.h"


int main () {
    Benefit *benefits = create_benefits();
    printf("created benefits\n");

    printf("first friend of apple is: %d\n", benefits[APPLE].friends[0]);
    
    int i, j;
    for (i=1; i < VARIETY; i++) {
        j=0;
        while (benefits[i].friends[j] != 0)
            j++;
        printf("%d ", j);
    }

    free_benefits(benefits);

    printf("\nFreed!\n");


    return 1;
}
