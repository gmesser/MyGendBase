def parse_bases(string, base):
    return int(string, base)

def print_bases(num):
    print(f"{num} (0b{bin(num)[2:]}, 0x{hex(num)[2:].upper()})")

