#create a module named as Arithmatic which contains 4 functions as Add() for addition, Sub() for substraction, Mult() for
#multiplication and Div() for division. All functions should accept two parameters as a number and perform the operation. write 
#on python program which call all the functions form Arithmatic module by accepting the parameter from user.
from Arithmatic import Add, Sub, Mult, Div

def main():
    if __name__ == "__main__":
        no1 = int(input("Enter a first number :"))
        no2 = int(input("Enter a second number :"))
        additionRes = Add(no1, no2)
        substractionRes = Sub(no1, no2)
        multiplicationRes = Mult(no1, no2)
        divisionRes = Div(no1, no2)

        print("Addition is :", additionRes)
        print("Substraction is :", substractionRes)
        print("Multiplication is :", multiplicationRes)
        print("Division is :", divisionRes)

main()