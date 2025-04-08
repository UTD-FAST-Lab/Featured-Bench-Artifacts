all: COMP_W2_D10_B256 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B256: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B256.c getHash.o -o COMP_W2_D10_B256


clean:
	rm COMP_W2_D10_B256 getHash.o
