#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void show(char *array[], int size) {
    int i;
    for (i=0; size > i; i++)
        printf("%s, ", array[i]);

    printf("\n");
}

void swap (char **x, char **y) {
    char *tmp = *x;
    *x = *y;
    *y = tmp;
}

unsigned long perm_size(int size) {
    unsigned long permutations = 1;
    int x;

    for (x=1; x <= size; x++)
        permutations = permutations * x;

    return permutations;
}

dict *perms(char *array[], int size) {
    dict *table;
    int size_of_table = 12354;
    int i;
    unsigned long count=0;
    unsigned long size_perm = perm_size(size) / 2; //ignore reverse cases
    
    // Create hash table
    table = create_dict(size_of_table);
    
    // go through perms, only one way
    while (count < size_perm) {
        for(i=0; i < size-1; i++) {
            swap(&array[i], &array[i+1]);
            count++;
        }
        swap(&array[0], &array[1]);
        count++;
    }
     
    return table;
}

