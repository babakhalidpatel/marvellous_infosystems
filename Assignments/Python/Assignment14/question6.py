#write a lambda function which accepts one number and returns True if number is odd otherwise false

oddNumber =  lambda no : no % 2 != 0

def main():
    if __name__ == "__main__":
        res = oddNumber(int(input("Enter a number :")))
        if res == True:
            print("Given number is odd")
        else:
            print("Given number is even")
main()