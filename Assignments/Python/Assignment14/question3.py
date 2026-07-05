#write a lambda function which accepts two numbers and returns maximum number
MaxNumber =  lambda no1,no2 : no1 > no2

def main():
    if __name__ == "__main__":
        res = MaxNumber(int(input("Enter first number :")),int(input("Enter second number :")))
        if res == True:
            print("First entered number is max")
        else:
            print("Second entered number is max")
main()