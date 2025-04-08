all: COMP_W2_D10_B512 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B512: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B512.c getHash.o -o COMP_W2_D10_B512


clean:
	rm COMP_W2_D10_B512 getHash.o
