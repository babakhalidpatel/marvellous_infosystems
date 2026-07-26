#write a program which accepts a file name from the user and counts how many lines are present in the file
import os
def CountLines(fileName):
    try:
        if os.path.isfile(fileName):
            fobj = open(fileName, "r")
            count = fobj.readlines()
            return len(count)
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    fileName = input("Enter File Name :")
    counter = CountLines(fileName)
    if counter:
        print(f"Number of lines in a file {fileName} are {counter}")

if __name__ == "__main__":
    main()