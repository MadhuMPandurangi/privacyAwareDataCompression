import subprocess
import os


dictionaryName = input("Enter the dictionary file name: ")
# check whether the path found or not
if not os.path.exists(dictionaryName):                               
    print(f"Error: Dictionary file '{dictionaryName}' not found.")

fileName = input("Enter the file name to be compressed: ")
# check whether the path found or not
if not os.path.exists(fileName):
    print(f"Error: file path/name '{fileName}' not found.")

command = ["zstd", "-D", dictionaryName, fileName] 

try:
    subprocess.run(command, check=True)
    print("Zstd compression with dictionary completed successfully.")
except subprocess.CalledProcessError as e:
    print("Error occurred while running the command:", e)
