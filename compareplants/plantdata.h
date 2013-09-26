#include <stdlib.h>
#include "plantnums.h"

#define VARIETY 68

typedef struct Benefit {
    int friends[27];
    int foes[7];
} Benefit;


Benefit *create_benefits () {
    int i;
    Benefit *benefits = (Benefit *) malloc( sizeof(Benefit) * VARIETY);
    
    if (benefits == NULL) return NULL;
   
    benefits[APPLE] = (Benefit) {.friends = {CHIVES, MARIGOLD, GARLIC, 
        HORSERADISH, LEMON_BALM, MUSTARD, NASTURTIUMS, SPINACH, TANSY, YARROW},
        .foes = {GRASS, POTATOES} };
    benefits[APRICOT] = (Benefit) {.friends ={BASIL, MARIGOLD, GARLIC,
        NASTURTIUMS, SPINACH, STINGING_NETTLE, SUNFLOWER, YARROW}, .foes = {
        TOMATO} };
    benefits[ASPARAGUS] = (Benefit) {.friends = {BASIL, MARJORAM, PARSLEY,
        TOMATO}, .foes = {0} };
    benefits[BASIL] = (Benefit) {.friends = {APRICOT, ASPARAGUS, CHIVES,
        CUCUMBER, FENNEL, TOMATO}, .foes = {RUE, SILVERBEET} };
    benefits[BEANS] = (Benefit) {.friends = {BROCCOLI, BRUSSEL_SPROUTS,
        CABBAGES, CARROTS, CAULIFLOWER, CORN, CUCUMBER, MARIGOLD, GRAPE_VINE,
        LETTUCE, MARJORAM, PARSLEY, PEAS, POTATOES, ROSEMARY, SAGE, SAVORY}, 
        .foes = {CHIVES, FENNEL, GARLIC, ONIONS} };
    benefits[BROAD_BEANS] = (Benefit) {.friends = {BROCCOLI, BRUSSEL_SPROUTS,
        CABBAGES, CAULIFLOWER, CORN, LETTUCE, MARJORAM, POTATOES, SPINACH}, 
        .foes = {CHIVES, FENNEL, GARLIC, ONIONS} };
    benefits[BUSH_BEANS] = (Benefit) {.friends = {BEETS, BROCCOLI, 
        BRUSSEL_SPROUTS, CABBAGES, CAULIFLOWER, CELERY, CORN, CUCUMBER,
        MARJORAM, POTATOES, STRAWBERRY, SUNFLOWER}, .foes = {CHIVES, GARLIC,
        ONIONS} };
    benefits[CLIMBING_BEANS] = (Benefit) {.friends = {BROCCOLI, BRUSSEL_SPROUTS,
        CABBAGES, CAULIFLOWER, CORN, LETTUCE, MARJORAM, RADISH}, .foes = {BEETS,
        CHIVES, GARLIC, ONIONS, SUNFLOWER} };
    benefits[BEETS] = (Benefit) {.friends = {BUSH_BEANS, BROCCOLI, 
        BRUSSEL_SPROUTS, CABBAGES, CAULIFLOWER, LETTUCE, MARJORAM, ONIONS,
        POTATOES, SILVERBEET}, .foes = {CLIMBING_BEANS, TOMATO} };
    benefits[BORAGE] = (Benefit) {.friends = {BROCCOLI, BRUSSEL_SPROUTS,
        CABBAGES, CAULIFLOWER, CUCUMBER, PEAS, SQUASH, STRAWBERRY, TOMATO}, 
        .foes = {0} };
    benefits[BROCCOLI] = (Benefit) {.friends = {BEANS, BROAD_BEANS, BUSH_BEANS,
        CLIMBING_BEANS, BEETS, BORAGE, CORIANDER, CUCUMBER, DILL, MARIGOLD,
        MARJORAM, NASTURTIUMS, POTATOES, TOMATO}, .foes = {RUE, STRAWBERRY} };
    benefits[BRUSSEL_SPROUTS] = (Benefit) {.friends = {BEANS, BROAD_BEANS,
        BUSH_BEANS, CLIMBING_BEANS, BEETS, BORAGE, CORIANDER, CUCUMBER, DILL,
        MARIGOLD, MARJORAM, POTATOES, STRAWBERRY, SUNFLOWER}, .foes = {0} };
    benefits[CABBAGES] = (Benefit) {.friends = {BEANS, BROAD_BEANS, 
        CLIMBING_BEANS, BEETS, BORAGE, CHAMOMILE, CELERY, CORIANDER, DILL,
        CUCUMBER, MARIGOLD, LETTUCE, MARJORAM, NASTURTIUMS, ONIONS, PEAS,
        PENNYROYAL, POTATOES, ROSEMARY, SAGE}, .foes = {GARLIC, RUE, STRAWBERRY,
        TOMATO} };
    benefits[CHAMOMILE] = (Benefit) {.friends = {CABBAGES}, .foes = {MINTS} };
    benefits[CARROTS] = (Benefit) {.friends = {BEANS, CHIVES, CORIANDER,
        DILL, CORN, CUCUMBER, MARIGOLD, LETTUCE, MARJORAM, ONIONS, PEAS, RADISH,
        ROSEMARY, SAGE, TOMATO}, .foes = {0} };
    benefits[CAULIFLOWER] = (Benefit) {.friends = {BEANS, BROAD_BEANS,
        BUSH_BEANS, CLIMBING_BEANS, BEETS, BORAGE, CELERY, CORIANDER, CUCUMBER,
        DILL, MARJORAM, POTATOES, TOMATO}, .foes = {RUE, STRAWBERRY} };
    benefits[CELERY] = (Benefit) {.friends = {BUSH_BEANS, CABBAGES, CAULIFLOWER,
        MARJORAM, PEAS, TOMATO}, .foes = {POTATOES} };
    benefits[CHERRY] = (Benefit) {.friends = {CHIVES, MARIGOLD, LETTUCE,
        NASTURTIUMS, SILVERBEET, SPINACH}, .foes = {POTATOES} };
    benefits[CHERVIL] = (Benefit) {.friends = {CORIANDER, DILL, GARLIC, LETTUCE,
        PARSLEY, RADISH, YARROW}, .foes = {0} };
    benefits[CHIVES] = (Benefit) {.friends = {APPLE, ASPARAGUS, CARROTS, CHERRY,
        FRUIT_TREES, MARJORAM, MULBERRY, ROSES, STRAWBERRY, TOMATO}, .foes = {
        BEANS, BROAD_BEANS, BUSH_BEANS, CLIMBING_BEANS, PEAS} };
    benefits[CORIANDER] = (Benefit) {.friends = {BROCCOLI, BRUSSEL_SPROUTS,
        CABBAGES, CHAMOMILE, CHERVIL}, .foes = {FENNEL} };
    benefits[CORN] = (Benefit) {.friends = {BEANS, BROAD_BEANS, BUSH_BEANS,
        CLIMBING_BEANS, CUCUMBER, MARJORAM, PEAS, POTATOES, PUMPKIN, RADISH,
        SQUASH, ZUCCHINI}, .foes = {0} };
    benefits[CUCUMBER] = (Benefit) {.friends = {BASIL, BEANS, BUSH_BEANS,
        BORAGE, BROCCOLI, BRUSSEL_SPROUTS, CABBAGES, CARROTS, CAULIFLOWER, CORN,
        LETTUCE, MARJORAM, NASTURTIUMS, PEAS, RADISH, SUNFLOWER}, .foes = {
        POTATOES, SAGE} };
    benefits[DILL] = (Benefit) {.friends = {BEETS, BROCCOLI, BRUSSEL_SPROUTS,
        CABBAGES, CARROTS, CAULIFLOWER, CELERY, CHERVIL, CORIANDER, DILL,
        CUCUMBER, FENNEL, TOMATO}, .foes = {0} };
    benefits[FENNEL] = (Benefit) {.friends = {BASIL, DILL}, .foes = {BEANS,
        BROAD_BEANS, CORIANDER, LAVENDER, TOMATO} };
    benefits[EGGPLANT] = (Benefit) {.friends = {BEANS, MARJORAM, POTATOES}, 
        .foes = {0} };
    benefits[MARIGOLD] = (Benefit) {.friends = {APPLE, APRICOT, BEANS, BROCCOLI,
        BRUSSEL_SPROUTS, CABBAGES, CAULIFLOWER, CHERRY, FRUIT_TREES, LETTUCE,
        MULBERRY, ROSES, STRAWBERRY, SUNFLOWER}, .foes = {0} };
    benefits[FRUIT_TREES] = (Benefit) {.friends = {CARROTS, CHIVES, MARIGOLD,
        GARLIC, NASTURTIUMS, SILVERBEET, SPINACH, STINGING_NETTLE, YARROW}, 
        .foes = {0} };
    benefits[GARLIC] = (Benefit) {.friends = {APPLE, APRICOT, CHERRY,
        FRUIT_TREES, MULBERRY, ROSEMARY, ROSES}, .foes = {BEANS, BROAD_BEANS,
        BUSH_BEANS, CLIMBING_BEANS, CABBAGES, PEAS, STRAWBERRY} };
    benefits[GOOSEBERRY] = (Benefit) {.friends = {TOMATO}, .foes = {0} };
    benefits[GRAPE_VINE] = (Benefit) {.friends = {MULBERRY, TOMATO, YARROW}, 
        .foes = {0} };
    benefits[GRASS] = (Benefit) {.friends = {MULBERRY, YARROW}, .foes = {APPLE,
        APRICOT, CHERRY, FRUIT_TREES, SAGE} };
    benefits[HORSERADISH] = (Benefit) {.friends = {APPLE, APRICOT, CHERRY,
        POTATOES, ROSES, SUNFLOWER}, .foes = {0} };
    benefits[LAVENDER] = (Benefit) {.friends = {CABBAGES, GARLIC, MARJORAM,
        ROSES, SILVERBEET, STINGING_NETTLE}, .foes = {FENNEL} };
    benefits[LEEKS] = (Benefit) {.friends = {CARROTS, CELERY, MARJORAM, ONIONS},
        .foes = {0} };
    benefits[LEMON_BALM] = (Benefit) {.friends = {APPLE, APRICOT, CHERRY,
        FRUIT_TREES, MULBERRY, ROSES}, .foes = {0} };
    benefits[LETTUCE] = (Benefit) {.friends = {BEANS, BROAD_BEANS,
        CLIMBING_BEANS, BEETS, CABBAGES, CARROTS, CHERRY, CHERVIL, CUCUMBER,
        MARIGOLD, MARJORAM, ONIONS, PEAS, RADISH, STRAWBERRY}, .foes = {
        PARSLEY} };
    benefits[MARJORAM] = (Benefit) {.friends = {ASPARAGUS, BEANS, BROAD_BEANS,
        BUSH_BEANS, CLIMBING_BEANS, BEETS, BROCCOLI, BRUSSEL_SPROUTS, CABBAGES,
        CARROTS, CAULIFLOWER, CELERY, CHERVIL, CORIANDER, DILL, CUCUMBER,
        LETTUCE, ONIONS, PEAS, POTATOES, PUMPKIN, RADISH, STRAWBERRY, SPINACH,
        SQUASH, TOMATO, ZUCCHINI}, .foes = {0} };
    benefits[MINTS] = (Benefit) {.friends = {CABBAGES, TOMATO}, .foes = {
        CARROTS, PARSLEY} };
    benefits[MUSTARD] = (Benefit) {.friends = {APPLE, APRICOT, CHERRY,
        FRUIT_TREES, GRAPE_VINE, NASTURTIUMS}, .foes = {0} };
    benefits[NASTURTIUMS] = (Benefit) {.friends = {APPLE, APRICOT, BROCCOLI,
        CABBAGES, CHERRY, CUCUMBER, FRUIT_TREES, MULBERRY, POTATOES, RADISH,
        ROSES, SQUASH, TOMATO, ZUCCHINI}, .foes = {0} };
    benefits[MULBERRY] = (Benefit) {.friends = {CHIVES, MARIGOLD, GARLIC,
        GRAPE_VINE, GRASS, LEMON_BALM, MUSTARD, NASTURTIUMS, SILVERBEET,
        SPINACH, TANSY, YARROW}, .foes = {0} };
    benefits[ONIONS] = (Benefit) {.friends = {BEETS, CABBAGES, CARROTS, LETTUCE,
        MARJORAM, PARSLEY, ROSES, SAVORY, SILVERBEET, STRAWBERRY, TOMATO}, 
        .foes = {BEANS, BROAD_BEANS, BUSH_BEANS, CLIMBING_BEANS, PEAS} };
    benefits[PARSLEY] = (Benefit) {.friends = {ASPARAGUS, BEANS, CHIVES, ONIONS,
        ROSEMARY, ROSES, TOMATO}, .foes = {LETTUCE} };
    benefits[PARSNIP] = (Benefit) {.friends = {BEANS, CHIVES, CORIANDER, DILL,
        CORN, LETTUCE, MARJORAM, ONIONS, PEAS, POTATOES, RADISH, SAGE, TOMATO}, 
        .foes = {CARROTS, CELERY} };
    benefits[PEAS] = (Benefit) {.friends = {BEANS, BORAGE, CABBAGES, CARROTS,
        CELERY, CORN, CUCUMBER, LETTUCE, MARJORAM, PARSNIP, POTATOES, RASPBERRY,
        SAGE}, .foes = {CHIVES, GARLIC, ONIONS, SHALLOTS} };
    benefits[PENNYROYAL] = (Benefit) {.friends = {CABBAGES}, .foes = {0} };
    benefits[POTATOES] = (Benefit) {.friends = {BEANS, BROAD_BEANS, BUSH_BEANS,
        BEETS, BROCCOLI, BRUSSEL_SPROUTS, CABBAGES, CAULIFLOWER, CORN,
        MARIGOLD, MARJORAM, NASTURTIUMS, PEAS}, .foes = {APPLE, CELERY, CHERRY,
        CUCUMBER} };
    benefits[PUMPKIN] = (Benefit) {.friends = {CORN, MARJORAM}, .foes = {
        POTATOES} };
    benefits[RADISH] = (Benefit) {.friends = {CLIMBING_BEANS, CARROTS, CHERVIL,
        CORN, CUCUMBER, LETTUCE, MARJORAM, NASTURTIUMS}, .foes = {0} };
    benefits[RASPBERRY] = (Benefit) {.friends = {MARIGOLD, PEAS, RUE}, 
        .foes = {POTATOES} };
    benefits[ROSEMARY] = (Benefit) {.friends = {BEANS, CABBAGES, GARLIC, SAGE},
        .foes = {POTATOES, TOMATO} };
    benefits[ROSES] = (Benefit) {.friends = {CHIVES, MARIGOLD, GARLIC,
        NASTURTIUMS, ONIONS, PARSLEY, RUE, SAGE}, .foes = {0} };
    benefits[RUE] = (Benefit) {.friends = {CARROTS, ROSES}, .foes = {BASIL,
        BROCCOLI, CABBAGES, CAULIFLOWER, SAGE} };
    benefits[SAGE] = (Benefit) {.friends = {BEANS, CABBAGES, PEAS, ROSEMARY,
        ROSES, STRAWBERRY}, .foes = {CUCUMBER, RUE} };
    benefits[SAVORY] = (Benefit) {.friends = {BEANS, ONIONS}, .foes = {0} };
    benefits[SHALLOTS] = (Benefit) {.friends = {MARJORAM}, .foes = {BEANS,
        PEAS} };
    benefits[SILVERBEET] = (Benefit) {.friends = {BEETS, CHERRY, FRUIT_TREES,
        MARJORAM, MULBERRY, ONIONS}, .foes = {BASIL} };
    benefits[SPINACH] = (Benefit) {.friends = {APPLE, APRICOT, BROAD_BEANS,
        CHERRY, FRUIT_TREES, MARJORAM, MULBERRY, STRAWBERRY}, .foes = {0} };
    benefits[STRAWBERRY] = (Benefit) {.friends = {BUSH_BEANS, BORAGE,
        BRUSSEL_SPROUTS, CHIVES, MARIGOLD, LETTUCE, ONIONS, SAGE, SPINACH}, 
        .foes = {BROCCOLI, CABBAGES, CAULIFLOWER} };
    benefits[STINGING_NETTLE] = (Benefit) {.friends = {APRICOT, FRUIT_TREES,
        HORSERADISH, TOMATO}, .foes = {0} };
    benefits[SQUASH] = (Benefit) {.friends = {BORAGE, CORN, MARJORAM,
        NASTURTIUMS, SUNFLOWER, TANSY}, .foes = {0} };
    benefits[SUNFLOWER] = (Benefit) {.friends = {APRICOT, BUSH_BEANS,
        BRUSSEL_SPROUTS, CUCUMBER, SQUASH}, .foes = {CLIMBING_BEANS, GARLIC,
        POTATOES} };
    benefits[TANSY] = (Benefit) {.friends = {APPLE, ASPARAGUS, BORAGE, CABBAGES,
        CHERRY, CUCUMBER, FRUIT_TREES, GRAPE_VINE, MULBERRY, ROSES, SQUASH,
        YARROW}, .foes = {0} };
    benefits[THYME] = (Benefit) {.friends = {CABBAGES, ROSES}, .foes = {0} };
    benefits[TOMATO] = (Benefit) {.friends = {ASPARAGUS, BASIL, BORAGE,
        BROCCOLI, CARROTS, CAULIFLOWER, CELERY, CHIVES, MARIGOLD, GRAPE_VINE,
        MARJORAM, NASTURTIUMS, ONIONS, PARSLEY, STINGING_NETTLE}, 
        .foes = {APRICOT, BEETS, FENNEL, POTATOES, ROSEMARY} };
    benefits[YARROW] = (Benefit) {.friends = {APPLE, APRICOT, CHERRY,
        FRUIT_TREES, GRAPE_VINE, MULBERRY}, .foes = {0} };
    benefits[ZUCCHINI] = (Benefit) {.friends = {CORN, MARJORAM, NASTURTIUMS}, 
        .foes = {0} };

    return benefits;
}

void free_benefits (Benefit *benefits) {
    int i;
    
    if (benefits == NULL) return;
    
    free(benefits);
}



