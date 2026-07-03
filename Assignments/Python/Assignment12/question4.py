# write a program which accept one number and prints that many numbers starting from 1.

def PrintNumbers(no):

    for i in range(1,no+1):
        print(i)

def main():
    if __name__ == "__main__":
        PrintNumbers(int(input("Enter a number :")))

main()