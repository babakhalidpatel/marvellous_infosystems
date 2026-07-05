#write a lambda function which accepts two numbers and returns multiplication

multiplication =  lambda no1, no2 : no1 * no2

def main():
    if __name__ == "__main__":
        res = multiplication(int(input("Enter first number :")),int(input("Enter second number :")))
        print("multiplication is :", res)
main()