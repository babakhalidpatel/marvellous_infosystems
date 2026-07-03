#write a program which accepts one number and prints count of digits in that number
def CountOfDigit(no):
    count = 0

    if no == 0:
        count = 1
    
    while no > 0:
        no = int(no / 10)
        count = count + 1
     
    
    print("Total numbers in given digit is :", count)


def maiin():
    if __name__ == "__main__":
        CountOfDigit(int(input("Enter a number: ")))
    
maiin()
