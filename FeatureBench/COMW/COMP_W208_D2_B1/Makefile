all: COMP_W208_D2_B1 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W208_D2_B1: getHash
	$(CC) $(CFLAGS) COMP_W208_D2_B1.c getHash.o -o COMP_W208_D2_B1


clean:
	rm COMP_W208_D2_B1 getHash.o
