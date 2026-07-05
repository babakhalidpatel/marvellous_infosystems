#write a lambda function which accepts one number and returns square of that number
squareNumber =  lambda no : no * no

def main():
    if __name__ == "__main__":
        res = squareNumber(int(input("Enter a number :")))
        print("Square of given number is :", res)
main()