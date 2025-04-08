#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "getHash.h"

void COMP_W2_D6_B1(unsigned hash)
{
    if (hash < 32) {
        if (hash < 16) {
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
        } else if (hash < 32) {
            if (hash < 24) {
                if (hash < 20) {
                    if (hash < 18) {
                        if (hash < 17) {
                            printf("this is branch 17\n");
                        } else if (hash < 18) {
                            printf("this is branch 18\n");
                        }
                    } else if (hash < 20) {
                        if (hash < 19) {
                            printf("this is branch 19\n");
                        } else if (hash < 20) {
                            printf("this is branch 20\n");
                        }
                    }
                } else if (hash < 24) {
                    if (hash < 22) {
                        if (hash < 21) {
                            printf("this is branch 21\n");
                        } else if (hash < 22) {
                            printf("this is branch 22\n");
                        }
                    } else if (hash < 24) {
                        if (hash < 23) {
                            printf("this is branch 23\n");
                        } else if (hash < 24) {
                            printf("this is branch 24\n");
                        }
                    }
                }
            } else if (hash < 32) {
                if (hash < 28) {
                    if (hash < 26) {
                        if (hash < 25) {
                            printf("this is branch 25\n");
                        } else if (hash < 26) {
                            printf("this is branch 26\n");
                        }
                    } else if (hash < 28) {
                        if (hash < 27) {
                            printf("this is branch 27\n");
                        } else if (hash < 28) {
                            printf("this is branch 28\n");
                        }
                    }
                } else if (hash < 32) {
                    if (hash < 30) {
                        if (hash < 29) {
                            printf("this is branch 29\n");
                        } else if (hash < 30) {
                            printf("this is branch 30\n");
                        }
                    } else if (hash < 32) {
                        if (hash < 31) {
                            printf("this is branch 31\n");
                        } else if (hash < 32) {
                            printf("this is branch 32\n");
                        }
                    }
                }
            }
        }
    } else if (hash < 64) {
        if (hash < 48) {
            if (hash < 40) {
                if (hash < 36) {
                    if (hash < 34) {
                        if (hash < 33) {
                            printf("this is branch 33\n");
                        } else if (hash < 34) {
                            printf("this is branch 34\n");
                        }
                    } else if (hash < 36) {
                        if (hash < 35) {
                            printf("this is branch 35\n");
                        } else if (hash < 36) {
                            printf("this is branch 36\n");
                        }
                    }
                } else if (hash < 40) {
                    if (hash < 38) {
                        if (hash < 37) {
                            printf("this is branch 37\n");
                        } else if (hash < 38) {
                            printf("this is branch 38\n");
                        }
                    } else if (hash < 40) {
                        if (hash < 39) {
                            printf("this is branch 39\n");
                        } else if (hash < 40) {
                            printf("this is branch 40\n");
                        }
                    }
                }
            } else if (hash < 48) {
                if (hash < 44) {
                    if (hash < 42) {
                        if (hash < 41) {
                            printf("this is branch 41\n");
                        } else if (hash < 42) {
                            printf("this is branch 42\n");
                        }
                    } else if (hash < 44) {
                        if (hash < 43) {
                            printf("this is branch 43\n");
                        } else if (hash < 44) {
                            printf("this is branch 44\n");
                        }
                    }
                } else if (hash < 48) {
                    if (hash < 46) {
                        if (hash < 45) {
                            printf("this is branch 45\n");
                        } else if (hash < 46) {
                            printf("this is branch 46\n");
                        }
                    } else if (hash < 48) {
                        if (hash < 47) {
                            printf("this is branch 47\n");
                        } else if (hash < 48) {
                            printf("this is branch 48\n");
                        }
                    }
                }
            }
        } else if (hash < 64) {
            if (hash < 56) {
                if (hash < 52) {
                    if (hash < 50) {
                        if (hash < 49) {
                            printf("this is branch 49\n");
                        } else if (hash < 50) {
                            printf("this is branch 50\n");
                        }
                    } else if (hash < 52) {
                        if (hash < 51) {
                            printf("this is branch 51\n");
                        } else if (hash < 52) {
                            printf("this is branch 52\n");
                        }
                    }
                } else if (hash < 56) {
                    if (hash < 54) {
                        if (hash < 53) {
                            printf("this is branch 53\n");
                        } else if (hash < 54) {
                            printf("this is branch 54\n");
                        }
                    } else if (hash < 56) {
                        if (hash < 55) {
                            printf("this is branch 55\n");
                        } else if (hash < 56) {
                            printf("this is branch 56\n");
                        }
                    }
                }
            } else if (hash < 64) {
                if (hash < 60) {
                    if (hash < 58) {
                        if (hash < 57) {
                            printf("this is branch 57\n");
                        } else if (hash < 58) {
                            printf("this is branch 58\n");
                        }
                    } else if (hash < 60) {
                        if (hash < 59) {
                            printf("this is branch 59\n");
                        } else if (hash < 60) {
                            printf("this is branch 60\n");
                        }
                    }
                } else if (hash < 64) {
                    if (hash < 62) {
                        if (hash < 61) {
                            printf("this is branch 61\n");
                        } else if (hash < 62) {
                            printf("this is branch 62\n");
                        }
                    } else if (hash < 64) {
                        if (hash < 63) {
                            printf("this is branch 63\n");
                        } else if (hash < 64) {
                            printf("this is branch 64\n");
                        }
                    }
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

    COMP_W2_D6_B1(getHash(data, size));

    free(data);

    return 0;
}
