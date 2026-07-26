#write a program which accepts a file name from the user , opens that file, and displays the entire contents on the console
import os
def CountLines(fileName):
    try:
        if os.path.isfile(fileName):
            fobj = open(fileName, "r")
            return fobj.read()
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    fileName = input("Enter File Name :")
    content = CountLines(fileName)
    if content:
        print(f"Contents are :")
        print(content)

if __name__ == "__main__":
    main()