
with open("dict2.zst",'rb') as f1:
    
    # reading f1 contents
    S = f1.read()
    print(S)
    print('\n\n')
    hex_string =  S.hex()
    print(hex_string)
    print('\n\n')
    # hex_bytes = bytes.fromhex(hex_string)
    # print(hex_bytes)

    


    # Adding 32

    # Split the string into pairs (e.g., "37", "a4", "30", ...)
    hex_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

    # Add 32 (0x20) to each pair, convert to integers, and back to hexadecimal
    modified_hex_pairs = [format((int(pair, 16) + 32) % 256, '02x') for pair in hex_pairs]

    # Join the modified pairs back into a single string
    result_hex_string = ''.join(modified_hex_pairs)

    # Print the result
    print(result_hex_string)
    print('\n\n')


    # converting back to bytes

    # Convert the hexadecimal string to bytes
    hex_string = bytes.fromhex(result_hex_string)
    
    print(hex_string)
    print('\n\n')



    # subtracting 32

    # Split the string into pairs (e.g., "37", "a4", "30", ...)
    hex_pairs = [result_hex_string[i:i+2] for i in range(0, len(result_hex_string), 2)]

    # Add 32 (0x20) to each pair, convert to integers, and back to hexadecimal
    modified_hex_pairs = [format((int(pair, 16) - 32) % 256, '02x') for pair in hex_pairs]

    # Join the modified pairs back into a single string
    result_hex_string = ''.join(modified_hex_pairs)

    # Print the result
    print(result_hex_string)
    print('\n\n')



    # converting back to bytes

    # Convert the hexadecimal string to bytes
    hex_string = bytes.fromhex(result_hex_string)
    
    print(hex_string)
    print('\n\n')

