'''
Take the following IPv4 address: 128.32.10.1
This address has 4 octets where each octet is a single byte (or 8 bits).
1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001
Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361
Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
'''
from math import log2, log10
from random import randrange

# Function 1 - Binary to decimal
def binaryToDecimal(binary):
    N = len(str(binary))
    decimal = 0
    for i in range(N):
        decimal += int(str(binary)[i]) * (2 ** (N-1-i))
    return str(decimal)                # Return string

# Function 2 - Decimal to binary
def decimalToBinary(decimal):
    if decimal == 0:
        return "0"
    N = int(log2(decimal)) + 1
    binary = []
    for i in range(N-1, -1, -1):
        if decimal >= 2 ** i:
            binary.append(str(1))
            decimal -= 2 ** i
        else:
            binary.append(str(0))
    return ''.join(binary)              # Return string


# Function 3 - Int32 to IP
def int32ToIP(int32):
    if int32ToIP == 0:
        return "0.0.0.0"
    # int32 is 2149583361 for example ---> maybe its binary representation is not 32 bytes --->
    # we have to fill up with 0's in the beginning of the binary word
    binary = decimalToBinary(int32)
    N = len(binary)
    filledBinary = []
    if len(binary) < 32:
        # We have to fill up with zeros
        filledBinary = [str(0) for i in range(32-N)]
    # Now, my new variable is a string with 0s and 1s with length 32
    filledBinary.extend(binary)
    filledBinary = ''.join(filledBinary)
    # Filled binary is a 32bit-string like this:  10000000001000000000101000000001
    binary1 = filledBinary[0:8]
    binary2 = filledBinary[8:16]
    binary3 = filledBinary[16:24]
    binary4 = filledBinary[24:]
    decimal1 = binaryToDecimal(binary1)
    decimal2 = binaryToDecimal(binary2)
    decimal3 = binaryToDecimal(binary3)
    decimal4 = binaryToDecimal(binary4)
    print(int32)
    return str(decimal1) + "." + str(decimal2) + "." +str(decimal3) + "." +str(decimal4)

# MAIN FUNCTION
int32_0 = 2149583361
print(int32ToIP(int32_0))
print()
int32_00 = 16
print(int32ToIP(int32_00))
print()
int32_1 = randrange(2**32)
print(int32ToIP(int32_1))
print()
int32_2 = randrange(2**32)
print(int32ToIP(int32_2))
print()
int32_3 = randrange(2**32)
print(int32ToIP(int32_3))
print()
int32_4 = randrange(2**32)
print(int32ToIP(int32_4))
print()