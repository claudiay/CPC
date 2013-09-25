#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS     10

void *compare_neighbors(char *array[], int x, int y, int size) {
    printf("I am running.\n");

    pthread_exit(NULL);
}

void *run() {
    pthread_t threads[NUM_THREADS];
    int rc;
    long i;

    for (i=0; i < NUM_THREADS; i++) {
        rc = pthread_create(threads + t, NULL, print_hello, (void *) t);
        if (rc) {
            printf("ERROR; return code from pthread_create() is %d\n", rc);
            exit(-1);
        }
    }

    // wait for threads to finish
    for (i=0; i < NUM_THREADS; i++)
        pthread_join(threads[i], NULL);

    pthread_exit(NULL);
}





