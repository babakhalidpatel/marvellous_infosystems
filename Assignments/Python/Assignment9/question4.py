#write a program which accepts one number and prints cube of that number
def CubeOfNumber(num1):
    print("Cube of given number is :", num1 * num1 * num1)

def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        CubeOfNumber(no)
main()