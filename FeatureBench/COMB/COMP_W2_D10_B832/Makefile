all: COMP_W2_D10_B832 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B832: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B832.c getHash.o -o COMP_W2_D10_B832


clean:
	rm COMP_W2_D10_B832 getHash.o
