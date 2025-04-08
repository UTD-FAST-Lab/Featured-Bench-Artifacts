all: COMP_W2_D10_B1024 getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
COMP_W2_D10_B1024: getHash
	$(CC) $(CFLAGS) COMP_W2_D10_B1024.c getHash.o -o COMP_W2_D10_B1024


clean:
	rm COMP_W2_D10_B1024 getHash.o
