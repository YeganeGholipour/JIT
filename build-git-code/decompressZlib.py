#!/usr/bin/env python

import sys
import zlib

compressed_data = sys.stdin.buffer.read()
try:
    decompressed_data = zlib.decompress(compressed_data)
    if isinstance(decompressed_data, bytes):
        print(decompressed_data.decode('utf-8'))  # Try decoding as UTF-8
    else:
        print(decompressed_data.hex())
except UnicodeDecodeError:
    print(decompressed_data.hex())  # Print hexadecimal representation if decoding fails
