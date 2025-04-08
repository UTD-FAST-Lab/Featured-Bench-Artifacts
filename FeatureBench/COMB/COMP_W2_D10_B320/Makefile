all: COMP_W2_D10_B320 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B320: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B320.c getHash.o -o COMP_W2_D10_B320


clean:
	rm COMP_W2_D10_B320 getHash.o
