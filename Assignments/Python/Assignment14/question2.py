#write a lambda function which accepts one number and returns cube of that number
cubeNumber =  lambda no : no * no * no

def main():
    if __name__ == "__main__":
        res = cubeNumber(int(input("Enter a number :")))
        print("Cube of given number is :", res)
main()