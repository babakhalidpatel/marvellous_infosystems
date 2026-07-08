#write a program which contains one function that accept one number from user and returns True if number is divisible by 5 otherwise return false

def isDivisibleBy5(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    if __name__ == "__main__":
        res = isDivisibleBy5(int(input("Enter a Number :")))
        if res == True:
            print("True")
        else:
            print("False")

main()