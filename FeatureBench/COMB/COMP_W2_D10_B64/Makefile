all: COMP_W2_D10_B64 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B64: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B64.c getHash.o -o COMP_W2_D10_B64


clean:
	rm COMP_W2_D10_B64 getHash.o
