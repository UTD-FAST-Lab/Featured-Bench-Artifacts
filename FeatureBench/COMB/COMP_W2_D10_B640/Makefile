all: COMP_W2_D10_B640 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B640: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B640.c getHash.o -o COMP_W2_D10_B640


clean:
	rm COMP_W2_D10_B640 getHash.o
