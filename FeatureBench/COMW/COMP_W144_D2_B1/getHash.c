#include "getHash.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned
getHash(unsigned char *data, long size) {
    unsigned hash = 0;
    for (long i = 0; i < size; ++i) {
        hash += data[i];
        printf("hash: %d\n", hash);
    }
    
    return hash % (int)pow(144, 2);
}
