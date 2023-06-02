#!/usr/bin/python3

def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if ascii_val >= 97 and ascii_val <= 122:
            ascii_val -= 32
        print(chr(ascii_val), end="")
    print()
