# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, both input and output will be given as a signed integer type.
# They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.

def reverseBits(n):
    result = 0
    for _ in range(32):
        result <<= 1
        result += (n & 1)
        n >>= 1
    return result


if __name__ == "__main__":
    print(reverseBits(43261596))
