#frequency of a string in file
#write a program which accepts a file name and a string from the user and
#  counts the frequency of that string in the given file
import os

def countStringFrequency(filename, search_string):
    try:
        if os.path.isfile(filename):
            with open(filename, "r") as fobj:
                content = fobj.read()
                frequency = content.count(search_string)
                print(f"The string '{search_string}' appears {frequency} times in the file.")
        else:
            print("File not found")
    except:
        print("Error occurred while reading the file")

def main():
    filename = input("Enter the file name: ")
    search_string = input("Enter the string to search for: ")
    countStringFrequency(filename, search_string)

if __name__ == "__main__":
    main()