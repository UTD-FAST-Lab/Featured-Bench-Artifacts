all: COMP_W2_D10_B128 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B128: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B128.c getHash.o -o COMP_W2_D10_B128


clean:
	rm COMP_W2_D10_B128 getHash.o
