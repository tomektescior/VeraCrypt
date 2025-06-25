#!/usr/bin/env python3
"""
Simple XOR cipher example.
This demonstration script is not secure and is for educational purposes only.
"""

import sys


def xor_encrypt(data: bytes, key: bytes) -> bytes:
    key_len = len(key)
    return bytes([data[i] ^ key[i % key_len] for i in range(len(data))])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <text> <key>")
        sys.exit(1)
    text, key = sys.argv[1].encode(), sys.argv[2].encode()
    encrypted = xor_encrypt(text, key)
    print(encrypted.hex())
