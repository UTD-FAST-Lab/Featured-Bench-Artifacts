all: COMP_W2_D10_B608 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B608: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B608.c getHash.o -o COMP_W2_D10_B608


clean:
	rm COMP_W2_D10_B608 getHash.o
