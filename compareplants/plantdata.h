#include <stdlib.h>
#include "plantnums.h"

#define VARIETY 68


typedef struct Benefit {
    int friends[30];
    int foes[30];
} Benefit;

void add_benefit (Benefit *benefits, int id, int friendly[], int foey[],
        int size_friendly, int size_foey) {
    int i;

    for(i=0; i < size_friendly; i++)
        benefits[id].friends[i] = friendly[i];

    for(i=0; i < size_foey; i++)
        benefits[id].foes[i] = foey[i];
}

Benefit *create_benefits () {
    Benefit *benefits = (Benefit *) malloc( sizeof(Benefit) * VARIETY);
    
    if (benefits == NULL) return NULL;
   
    add_benefit(benefits, APPLE, {CHIVES, MARIGOLD, GARLIC, HORSERADISH,
            LEMON_BALM, MUSTARD, NASTURTIUMS, SPINACH, TANSY, YARROW}, {GRASS,
            POTATOES}, 10, 2);
    add_benefit(benefits, APRICOT, {BASIL, MARIGOLD, GARLIC, NASTURTIUM,
            SPINACH, STINGING_NETTLE, SUNFLOWER, YARROW}, {TOMATO}, 8, 1);
    add_benefit(benefits, ASPARAGUS, {BASIL, MARJORAM, PARSLEY, TOMATO},
            {0}, 4, 1);
    add_benefit(benefits, BASIL, {APRICOT, ASPARAGUS, CHIVES, CUCUMBER,
            FENNEL, TOMATO}, {RUE, SILVERBEET}, 6, 2);
    
    return benefits;
}

void free_benefits (Benefit *benefits) {
    int i;
    
    if (benefits == NULL) return;
    
    free(benefits);
}



