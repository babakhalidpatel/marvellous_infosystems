#write a lambda function which accepts one number and returns True if number is even otherwise false
EvenNumber =  lambda no : no %2 == 0

def main():
    if __name__ == "__main__":
        res = EvenNumber(int(input("Enter a number :")))
        if res == True:
            print("Given number is even")
        else:
            print("Given number is odd")
main()