#write a program which accept one number from user and return its factorial

def factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    return fact

def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        fact = factorial(no)
        print("Factorial is :", fact)

main()