#write a program which accepts a file name from the user and checks whether that file exist in the current directory or not

import os
def CheckFileExistance(fileName):
    try:
        if os.path.isfile(fileName):
            return True
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    fileName = input("Enter File Name :")
    exist = CheckFileExistance(fileName)
    if exist:
        print(f"Yes file exist")

if __name__ == "__main__":
    main()