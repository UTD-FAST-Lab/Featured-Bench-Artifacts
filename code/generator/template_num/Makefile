all: FUNC getHash

getHash:
	echo $(CC)
	$(CC) $(CFLAGS) -c getHash.c -o getHash.o
FUNC: getHash
	$(CC) $(CFLAGS) FUNC.c getHash.o -o FUNC


clean:
	rm FUNC getHash.o
