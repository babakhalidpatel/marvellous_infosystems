#write a program which accept one number from user and return addition of digits in that number


def numberOfDigits(no):
    arr = str(no)
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        ans = numberOfDigits(no)
        print("Addition of digits are :", ans)
main()