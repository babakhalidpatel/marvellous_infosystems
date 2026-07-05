#write a lambda function which accepts one number and returns True if divisible by 5
divisibleBy5 =  lambda no : no % 5 == 0

def main():
    if __name__ == "__main__":
        res = divisibleBy5(int(input("Enter a number :")))
        if res == True:
            print("Number is divisible by 5")
        else:
            print("Number is not divisible by 5")
main()