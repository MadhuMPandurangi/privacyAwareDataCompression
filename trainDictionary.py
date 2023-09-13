import subprocess
import sys
import os


directory_path = "../textFiles"# input("Enter the directory path where text files are stored: ")
file_names = "a.txt b.txt c.txt d.txt e.txt f.txt g.txt".split() # input("Enter the file names separated by spaces: ").split()

file_paths = [os.path.join(directory_path, file_name) for file_name in file_names]

command = ["zstd", "--train", "-B1M"] + file_paths

try:
    subprocess.run(command, check=True)
    print("=====================================")
    print("Zstd training completed successfully.")
    print("=====================================")
except subprocess.CalledProcessError as e:
    print("Error occurred while running the command:", e)
