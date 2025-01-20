SRC=src/*.c
BIN=bin
EXEC=mmcc
CCOMPILER=gcc
CFLAGS=-o $(BIN)/$(EXEC) $(SRC)

compile:
	@echo "Compiling..."
	mkdir -p $(BIN)
	$(CCOMPILER) $(CFLAGS)
	@echo "Done."
