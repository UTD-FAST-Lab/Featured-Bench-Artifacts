#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "getHash.h"

void COMP_W2_D2_B1(unsigned hash)
{
    if (hash < 2) {
        if (hash < 1) {
            printf("this is branch 1\n");
            int *ptr = NULL;
            *ptr = 10;
        } else if (hash < 2) {
            printf("this is branch 2\n");
        }
    } else if (hash < 4) {
        if (hash < 3) {
            printf("this is branch 3\n");
        } else if (hash < 4) {
            printf("this is branch 4\n");
        }
    }

}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *fp = fopen(argv[1], "rb");
    if (fp == NULL)
    {
        perror("Error opening file");
        return 1;
    }

    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    rewind(fp);
    printf("size: %ld\n", size);

    unsigned char *data = malloc(size * sizeof(unsigned char));
    if (data == NULL)
    {
        fprintf(stderr, "Error allocating memory\n");
        fclose(fp);
        return 1;
    }

    if (fread(data, sizeof(unsigned char), size, fp) != size)
    {
        fprintf(stderr, "Error reading file\n");
        fclose(fp);
        free(data);
        return 1;
    }

    COMP_W2_D2_B1(getHash(data, size));

    free(data);

    return 0;
}
