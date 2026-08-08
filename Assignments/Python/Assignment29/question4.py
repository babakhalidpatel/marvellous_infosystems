#compare two files
#write a program which accepts two file names through command 
# line arguments and compares the contents of both files. 
# If both files are same then it should display "Success" otherwise 
# it should display "Failure"

import os
import sys
def compareFiles(file1, file2):
    try:
        if os.path.isfile(file1) and os.path.isfile(file2):
            fobj1 = open(file1, "r")
            fobj2 = open(file2, "r")
            content1 = fobj1.read()
            content2 = fobj2.read()
            if content1 == content2:
                print("Success")
            else:
                print("Failure")
        else:
            print("One or both files not found")
    except:
        print("Error occurred while comparing files")


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1> <file2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compareFiles(file1, file2)

if __name__ == "__main__":
    main()