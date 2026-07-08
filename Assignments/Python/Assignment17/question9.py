#write a program which accept one number from user and return number of digits in that number


def numberOfDigits(no):
    return len(str(no))


def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        ans = numberOfDigits(no)
        print("Number of digits are :", ans)
main()