#write a program which accepts two file name from a user
#first file is an existing file
#second file is a new file
#copy all contents from the first file into new file
import os
def copyContents(firstFile, secondFile):
    try:
        if os.path.isfile(firstFile):
            fobj = open(firstFile, "r")
            count = fobj.readlines()
            sobj = open(secondFile, "w")
            sobj.writelines(count)
            return True
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    firstFile = input("Enter Existing File Name :")
    secondFile = input("Enter New file Name :")
    contents = copyContents(firstFile, secondFile)
    if contents:
        print(f"Content copied")

if __name__ == "__main__":
    main()