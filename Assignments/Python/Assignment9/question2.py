#write a program which contain one function chkgreater that accepts two numbers and print the greater number
#Input: 10 20
#Output: 20 is greater
def CheckGreater(num1, num2):
    if num1 > num2:
        print(num1, "is greater")
    elif num1 == num2:
        print("Both are same")
    else:
        print(num2, "is greater")



def main():
    if __name__ == "__main__":
        no1 = int(input("Enter first number : "))
        no2 = int(input("Enter second number : "))
        CheckGreater(no1,no2)

main()