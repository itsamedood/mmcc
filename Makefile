MAIN=src/main.py
FLAGS=-B
TARGET_DIR=bin
TARGET_NAME=mmcc

compile:
	@echo "Compiling..."
	mkdir -p $(TARGET_DIR)
	cxfreeze --target-dir $(TARGET_DIR) --target-name $(TARGET_NAME) $(MAIN)
	@echo "Done."
