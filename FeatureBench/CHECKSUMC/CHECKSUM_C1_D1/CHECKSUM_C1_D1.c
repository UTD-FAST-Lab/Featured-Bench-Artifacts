#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>


uint64_t sum(const unsigned char *data, size_t length) {
    uint64_t result = 0;
    for (size_t i = 0; i < length; i++) {
        result += data[i];
    }
    return result;
}

uint64_t average(const unsigned char *data, size_t length) {
    uint64_t total = 0;
    for (size_t i = 0; i < length; i++) {
        total += data[i];
    }
    return total / length;
}

uint64_t product(const unsigned char *data, size_t length) {
    uint64_t result = 1;
    for (size_t i = 0; i < length; i++) {
        result *= data[i];
    }
    return result;
}

uint64_t u64(const unsigned char *data) {
    uint64_t value = 0;
    for (size_t i = 0; i < 8; i++) {
        value |= (uint64_t)data[i] << (i * 8);
    }
    return value;
}

uint32_t u32(const unsigned char *data) {
    uint32_t value = 0;
    for (size_t i = 0; i < 4; i++) {
        value |= ((uint32_t)data[i] << (i * 8));
    }
    return value;
}

uint16_t u16(const unsigned char *data) {
    uint16_t value = 0;
    for (size_t i = 0; i < 2; i++) {
        value |= ((uint16_t)data[i] << (i * 8));
    }
    return value;
}

void CHECKSUM_C1_D1(unsigned char *data, long size)
{
    if (size < 16) {
        printf("File is too small...");
        return;
    }
    if (u64(data) == sum(data+8, 8)) {
        printf("Found magic symbol!");
        int *ptr = NULL;
        *ptr = 10;
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

    CHECKSUM_C1_D1(data, size);

    free(data);

    return 0;
}
