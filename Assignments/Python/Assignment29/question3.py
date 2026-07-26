#write a program which accepts an existing file name through command line arguments , creates a new file named Demo.txt 
# and copies all contents from the given file into Demo.txt
import os
import sys
def copyFiles(fileName):
    try:
        if os.path.isfile(fileName):
            fobj = open(fileName, "r")
            count = fobj.readlines()
            sobj = open("Demo.txt","w")
            sobj.writelines(count)
            print("File copied")
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    fileName = sys.argv[1]
    copyFiles(fileName)

if __name__ == "__main__":
    main()