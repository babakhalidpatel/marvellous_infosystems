#write a program which accepts a file name from the user and counts total number of words in the file
import os
def CountWords(fileName):
    try:
        if os.path.isfile(fileName):
            fobj = open(fileName, "r")
            count = fobj.read()
            return len(count.split())
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    fileName = input("Enter File Name :")
    counter = CountWords(fileName)
    if counter:
        print(f"Number of words in a file {fileName} are {counter}")

if __name__ == "__main__":
    main()