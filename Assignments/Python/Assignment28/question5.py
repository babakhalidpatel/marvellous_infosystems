#write a program which accepts a file name from the user and a word from user and checks whether that word is present in that file or not
import os
def SearchAWordInAFile(fileName, wordName):
    try:
        if os.path.isfile(fileName):
            fobj = open(fileName, "r")
            count = fobj.read()
            if wordName in count.split():
                print(f"{wordName} Found in a file")
            else:
                print(f"{wordName} not found")
        else:
            print("File Not found")
    except:
        print("File Not found")


def main():
    fileName = input("Enter File Name :")
    wordName = input("Enter a word name :")
    SearchAWordInAFile(fileName, wordName)

if __name__ == "__main__":
    main()