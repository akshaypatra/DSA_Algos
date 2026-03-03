bit_s = '1010'

# Convert binary string into an integer
temp = int(bit_s, 2)

# XOR with 2^(n+1) - 1 to invert bits
inv_s = temp ^ (2 ** (len(bit_s)) - 1)

# Convert the result back to binary and strip the '0b' prefix
res = bin(inv_s)[2:]

print("Inversed string is", res)