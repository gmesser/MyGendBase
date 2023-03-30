# Geerated base program.

import sys

print("Python!")

def parse_bases(num_str):
    num = int(num_str, 0)
    return (bin(num), num, hex(num))

def print_bases(num):
    print("Base 2:", bin(num))
    print("Base 10:", num)
    print("Base 16:", hex(num))

def process_number(num_str):
    bases = parse_bases(num_str)
    print("Number in different bases:")
    print("Binary:", bases[0])
    print("Decimal:", bases[1])
    print("Hexadecimal:", bases[2])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_number.py <number>")
    else:
        process_number(sys.argv[1])

