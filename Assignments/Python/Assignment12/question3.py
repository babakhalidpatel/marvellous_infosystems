# Write a program which accepts two numbers and print addition, substraction, multiplication and division

def AddSubMulDiv(no1, no2):

    print("Addition is :", no1 + no2)
    print("Substraction is :", no1 - no2)
    print("Multiplication is :", no1 * no2)
    print("Division is :", no1 / no2)

def main():
    if __name__ == "__main__":
        AddSubMulDiv(int(input("Enter first number :")), int(input("Enter second number :")))

main()
