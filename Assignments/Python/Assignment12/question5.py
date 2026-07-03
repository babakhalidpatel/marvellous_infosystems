# write a program which accept one number and prints that many numbers in reverse order.

def PrintNumbersInReverse(no):

    for i in range(1,no+1):
            print((no + 1) - i)

def main():
    if __name__ == "__main__":
        PrintNumbersInReverse(int(input("Enter a number :")))

main()