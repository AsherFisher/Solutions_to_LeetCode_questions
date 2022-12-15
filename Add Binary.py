# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a, b):
    return str(int(bin(int(a, 2) + int(b, 2))[2:]))


if __name__ == "__main__":
    print(addBinary("11", "1"))
