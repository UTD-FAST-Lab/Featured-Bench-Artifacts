#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "getHash.h"

void COMP_W2_D4_B1(unsigned hash)
{
    if (hash < 8) {
        if (hash < 4) {
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
        } else if (hash < 8) {
            if (hash < 6) {
                if (hash < 5) {
                    printf("this is branch 5\n");
                } else if (hash < 6) {
                    printf("this is branch 6\n");
                }
            } else if (hash < 8) {
                if (hash < 7) {
                    printf("this is branch 7\n");
                } else if (hash < 8) {
                    printf("this is branch 8\n");
                }
            }
        }
    } else if (hash < 16) {
        if (hash < 12) {
            if (hash < 10) {
                if (hash < 9) {
                    printf("this is branch 9\n");
                } else if (hash < 10) {
                    printf("this is branch 10\n");
                }
            } else if (hash < 12) {
                if (hash < 11) {
                    printf("this is branch 11\n");
                } else if (hash < 12) {
                    printf("this is branch 12\n");
                }
            }
        } else if (hash < 16) {
            if (hash < 14) {
                if (hash < 13) {
                    printf("this is branch 13\n");
                } else if (hash < 14) {
                    printf("this is branch 14\n");
                }
            } else if (hash < 16) {
                if (hash < 15) {
                    printf("this is branch 15\n");
                } else if (hash < 16) {
                    printf("this is branch 16\n");
                }
            }
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

    COMP_W2_D4_B1(getHash(data, size));

    free(data);

    return 0;
}
