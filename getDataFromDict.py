def getData(dictFile):
    with open(dictFile,'rb') as f1:
    
        # reading f1 contents
        S = f1.read()
        print(S)
        print(type(S))
        print("\n\n")

        hex_string =  S.hex()
        print(hex_string)
        print(type(hex_string))
        print("\n\n")



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




        # Find the index where (0000 0004 0000 0008 0000 00)+32 = "2020 2024 2020 2028 2020 20" appears in the string
        index = result_hex_string.find("2020202420202028202020")

        # Check if the substring was found
        if index != -1:
            # Extract the data after "2020202420202028202020"
            data_after_substring = result_hex_string[index + len("2020202420202028202020"):]

            # Print the extracted data
            print(data_after_substring)
            print("\n")
        else:
            print("Data not found in the input string.")



