all: COMP_W2_D10_B288 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B288: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B288.c getHash.o -o COMP_W2_D10_B288


clean:
	rm COMP_W2_D10_B288 getHash.o
