all: COMP_W2_D10_B32 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B32: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B32.c getHash.o -o COMP_W2_D10_B32


clean:
	rm COMP_W2_D10_B32 getHash.o
