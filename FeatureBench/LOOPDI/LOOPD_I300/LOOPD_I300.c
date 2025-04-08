#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

void LOOPD_I300(unsigned char *data, long size)
{
    for (unsigned int i = 0; i < size; i++) {
        printf("this is iteration %d\n", i);
        if (data[i] == 'a') {
            if (i == 300) {
                printf("Crash!\n");
                int *p = NULL;
                *p = 10;
            }
        } else {
            break;
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

    LOOPD_I300(data, size);

    free(data);

    return 0;
}
