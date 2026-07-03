#write a program which accepts one number and prints square of that number
def SquareOfNumber(num1):
    print("Square of given number is :", num1 * num1)

def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        SquareOfNumber(no)
main()