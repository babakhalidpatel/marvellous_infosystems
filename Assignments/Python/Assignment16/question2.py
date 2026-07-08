#write a program which contains one function named as ChkNum() which accept one parameter as a number. if number is even then it should disaply "Even Number"
#otherwise display "Odd Number" on console

def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    if __name__ == "__main__":
        ChkNum(int(input("Enter a number :")))

main()