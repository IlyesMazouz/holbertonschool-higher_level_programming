#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        ascii_val = ord(char)
        if ascii_val >= 97 and ascii_val <= 122:
            ascii_val -= 32
        result += chr(ascii_val)
    print(f"{result}\n", end="")

