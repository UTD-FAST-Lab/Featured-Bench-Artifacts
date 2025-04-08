#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

void MAGIC_S0_L1_D6(unsigned char *data, long size)
{
    if (size < 6) {
        printf("File is too small...");
        return;
    }
    if ((data[0]) == '<') {
        if ((data[1]) == '&') {
            if ((data[2]) == '*') {
                if ((data[3]) == '+') {
                    if ((data[4]) == '/') {
                        if ((data[5]) == '-') {
                            printf("Found magic symbol!");
                            int *ptr = NULL;
                            *ptr = 10;
                        }
                    }
                }
            }
        }
    } else {
        printf("Not magic symbol, continue...");
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

    MAGIC_S0_L1_D6(data, size);

    free(data);

    return 0;
}
