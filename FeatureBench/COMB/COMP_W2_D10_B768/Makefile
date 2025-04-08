all: COMP_W2_D10_B768 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B768: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B768.c getHash.o -o COMP_W2_D10_B768


clean:
	rm COMP_W2_D10_B768 getHash.o
