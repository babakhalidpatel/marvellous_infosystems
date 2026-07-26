#write a program which accepts a file name from the user and displays the contents of a file line by line on the screen
import os
def FileContentsLineByLine(fileName):
    try:
        if os.path.isfile(fileName):
            fobj = open(fileName, "r")
            count = fobj.read()
            return count
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    fileName = input("Enter File Name :")
    contents = FileContentsLineByLine(fileName)
    if contents:
        print(f"File contects are below :")
        print(contents)


if __name__ == "__main__":
    main()