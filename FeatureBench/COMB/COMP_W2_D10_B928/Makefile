all: COMP_W2_D10_B928 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B928: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B928.c getHash.o -o COMP_W2_D10_B928


clean:
	rm COMP_W2_D10_B928 getHash.o
