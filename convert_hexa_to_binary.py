import binascii

# converting to hexa string binary

# Original bytes
S = b'7\xa40\xec\x00\x91\x80\x06\t\x10\x10\xdf033\xb3w\n'

# Convert bytes to hexadecimal string
hex_string = binascii.hexlify(S).decode('ascii')

# Convert hexadecimal string to binary string
binary_string = bin(int(hex_string, 16))[2:]

# Print the binary string
print(binary_string)