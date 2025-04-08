#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <binary_file> <output_directory>"
    exit 1
fi

BINARY_FILE="$1"
OUTPUT_DIR="$2"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Use objdump to disassemble, extract constants, and write them to files
objdump -d "$BINARY_FILE" | grep -Eo '\$0x[0-9a-f]{8}' | cut -c 2- | sort -u | while read -r const; do
    # Write packed data to the file
    echo "$const" | python3 -c '
import sys, struct

for l in sys.stdin:
    l = l.strip()
    if len(l) <= 10:  # Less than or equal to 10 includes 32-bit (8 digits + "0x")
        packed = struct.pack("<I", int(l, 0))  # 32-bit integer
    else:
        packed = struct.pack("<Q", int(l, 0))  # 64-bit integer
    sys.stdout.buffer.write(packed)
' > "${OUTPUT_DIR}/${const}"
done
