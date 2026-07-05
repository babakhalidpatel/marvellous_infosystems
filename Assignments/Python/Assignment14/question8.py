#write a lambda function which accepts two numbers and returns addition
addition =  lambda no1, no2 : no1 + no2

def main():
    if __name__ == "__main__":
        res = addition(int(input("Enter first number :")),int(input("Enter second number :")))
        print("addition is :", res)
main()