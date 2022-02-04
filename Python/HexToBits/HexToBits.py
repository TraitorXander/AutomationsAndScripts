import sys
import os
from bitstring import BitArray

def main():
    count = 0

    # print("Bytes for 22")
    # for x in hex_to_bits('22'):
    #     print(str(count) + " " + str(x))
    #     count+=1

    # ignore_bytes = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
    # print("Bytes for 00 22 00 02")
    # for x in hex_to_bits('00 22 00 02'):
    #     if(count not in ignore_bytes):
    #         print(str(count) + " " + str(x))
    #     count+=1

    ignore_bytes = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
    print("Bytes for 00 02 00 02")
    for x in hex_to_bits('00 02 00 02'):
        if(count not in ignore_bytes):
            print(str(count) + " " + str(x))
        count+=1

def hex_to_bits(input):
    c = BitArray(hex=input)
    return c.bin

if __name__ == "__main__":
    main()