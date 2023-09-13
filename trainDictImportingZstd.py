import zstandard as zstd

# List of file paths
file_paths = ['../textFiles/a.txt', '../textFiles/b.txt', '../textFiles/c.txt']  # Add your file paths here

# Initialize the dictionary builder
builder = zstd.ZstdDictBuilder()

# Read the contents of each file and add them to the builder
for file_path in file_paths:
    with open(file_path, 'rb') as f:
        file_content = f.read()
        builder.train_from_buffer(file_content)

# Build the dictionary
dictionary = builder.build()

# Save the trained dictionary to a file
with open('trained_dict.zdict', 'wb') as f:
    f.write(dictionary)

print("Dictionary trained and saved.")
