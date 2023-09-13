import os

def main():
    while True:
        print("---------------------------")
        print("Enter '1' to train")
        print("Enter '2' for compress")
        print("Enter '3' for decompress")
        print("Enter 'q' to quit")
        
        choice = input("Enter your choice: ")
        print("---------------------------")
        if choice == '1':
            os.system("python3 trainDictionary.py")
        elif choice == '2':
            os.system("python3 compress.py")
        elif choice == '3':
            os.system("python3 decompress.py")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
